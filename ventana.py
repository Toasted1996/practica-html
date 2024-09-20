import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0



#Configuracion de la ventana
ventana = turtle.Screen()
ventana.title('Snake Game')
ventana.bgcolor('Black')
ventana.setup(width=600, height=600)
ventana.tracer(0)


#Cabeza de la serpiente 
head = turtle.Turtle() 
head.speed(0) #define la velocidad de la cabeza
head.shape('square') #define la forma
head.penup() #puede mover el objeto sin dejar rastro
head.color('White') #color del objeto
head.goto(0,0) #comando para mover la tortuga u objeto a una posicion especifica
head.direction = 'stop'

#Cuerpo serpiente
segmento = []

#Texto Puntaje
text = turtle.Turtle()
text.speed(0)
text.color('White')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write ('Score: 0           High Score:0', align= 'center', font= ('courier', 20, 'normal'))

#Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('Red')
food.penup()
food.goto(0,100)


#Funciones 

def arriba():
    head.direction ='up'
def abajo ():
    head.direction = 'down'
def derecha(): 
    head.direction = 'right'
def izquierda(): 
    head.direction ='left'           

#Movimiento
 
def movimiento():
    if head.direction =='up':
        y = head.ycor() #Da la coordenada y de la cabeza
        head.sety(y + 20) #Ordena cuantos pixeles se mueve la cabeza 
      
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20) # Es menos 20 ya que es como un plano cartesiano
                
    if head.direction == 'left':
        x = head.xcor() #define donde esta posicionado el eje de X        
        head.setx(x - 20)
 
    if head.direction == 'right':
        x = head.xcor() 
        head.setx(x + 20)      

#Conexion teclado (Seguira las ordenes del teclado)
ventana.listen()
ventana.onkeypress(arriba,'Up')
ventana.onkeypress(abajo, 'Down')
ventana.onkeypress(derecha, 'Right')
ventana.onkeypress(izquierda, 'Left')

while True: 
    ventana.update()
    
    #Border Colision
    
    if head.xcor() > 280 or head.xcor() <-280 or head.ycor() > 280 or head.ycor() <-290: #Le da un limite a la serpiente dentro del plano cartesiano
        time.sleep(1) #Pequeña pausa al juego 
        head.goto(0,0) # Vuelve al punto inicial
        head.direction = 'stop' #Da la orden de parar
      
        #Esconder segmentos ganados (if lose)
        for total_body in segmento:
            total_body.goto(1000,1000)
        
        #Limpia lista de segmento 
        segmento.clear()
        
        #Reset marcador
        score = 0
        text.write  ('Score: {}             High Score:{}'.format(score, high_score), 
        align = 'center', font = ('courier', 20, 'normal'))
        
    
    
    if head.distance(food) < 20: #Choque de la comida, si es menos de 20px de distancia
        x = random.randint(-280,280) # Desaparece la comida y vuelve a aparecer en un lugar random de la ventana
        y = random.randint(-280,280)
        food.goto(x,y)
        body = turtle.Turtle() #Cada vez que pase por la comida, creara un nuevo segmento en el centro del plano 
        body.speed(0)
        body.shape('square')
        body.color('White')
        body.penup()
        segmento.append(body)
        
        
        
        #Aumento marcador
        score += 10
        
        if score > high_score:
            high_score = score

        
        text.clear()
        text.write  ('Score: {}            High Score:{}'.format(score, high_score), 
        align = 'center', font = ('courier', 20, 'normal'))
        
        
        
        
    #Movimiento cuerpo serpiente
    total_body = len(segmento) #Se toma la cuenta de los segmentos creados
    
    for index in range(total_body -1,0,-1): # Lo que hace es hacer un condeo desde el indice hasta el ultimo segmento creado
        x = segmento[index -1].xcor() 
        y = segmento[index -1].ycor()
        segmento[index].goto(x,y)
    
    if total_body > 0:
        x = head.xcor()
        y = head.ycor()
        segmento[0].goto(x,y)    
     
            
    movimiento()
    time.sleep(posponer)

    