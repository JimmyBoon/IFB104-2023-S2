from turtle import *
import math
setup()

things_i_want = [[200,200,"cross"],[-200,-200,"square"],[-200,200,"cross_square"],[200,-200,"circle_square"]]

def square():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

def cross():
    left(45)
    forward(math.sqrt(100**2 + 100**2))
    left(90)
    left(45)
    penup()
    forward(100)
    pendown()
    left(90)
    left(45)
    forward(math.sqrt(100**2 + 100**2))

def my_circle():
    penup()
    forward(-50)
    pendown()
    circle(50)



def draw_object_at(x_pos, y_pos, object):
    setheading(0)
    penup()
    goto(x_pos, y_pos)
    pendown()

    object()



hideturtle()
done()