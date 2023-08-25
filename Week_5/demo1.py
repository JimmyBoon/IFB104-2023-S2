from turtle import *
import math
setup()

things_i_want = [[200,200,"cross"],[-200,-200,"square"],[-200,200,"cross_square"],[200,-200,"circle_square"], [99,00, "dog"]]

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

speed('fastest')
for xPos, yPos, shape in things_i_want:
    if shape == 'cross':
        draw_object_at(xPos, yPos, cross)
        continue

    if shape == 'square':
        draw_object_at(xPos, yPos, square)
        continue

    if shape == 'cross_square':
        draw_object_at(xPos, yPos, square)
        draw_object_at(xPos, yPos, cross)
        continue

    if shape == 'circle_square':
        draw_object_at(xPos, yPos, square)
        draw_object_at(xPos + 100, yPos, my_circle)
        continue
    
    
#     print("Object not found")

# for thing in things_i_want:
#     possible_objects = ['square','cross', 'my_circle']
#     draw_object_at(thing[0], thing[1], eval(thing[2])) if thing[2] in possible_objects else print(f'cant draw {thing[2]} :(')

hideturtle()
done()