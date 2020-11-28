import turtle
import time 

def drawKochSide(length, level):
    if (level == 1):
        turtle.forward(length)
    else:
        drawKochSide(length/3, level-1)
        turtle.left(60)
        drawKochSide(length/3, level-1)
        turtle.right(120)
        drawKochSide(length/3, level-1)
        turtle.left(60)
        drawKochSide(length/3, level-1)

def drawKochSnowflake(length, level):
    for step in range(3):
        drawKochSide(length, level)
        turtle.right(120)

def draw():
    turtle.delay(1)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    #time.sleep(5)
    turtle.pencolor('black')
    drawKochSide(300, 4)

    turtle.pencolor('blue')
    drawKochSnowflake(300, 4)

    turtle.penup()
    turtle.goto(-250,50)
    turtle.pendown()

    turtle.pencolor('red')
    drawKochSnowflake(200, 5)

    turtle.done()

draw()