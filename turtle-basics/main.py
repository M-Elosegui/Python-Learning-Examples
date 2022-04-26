####### RANDOM LINES DRAWING

# from turtle import Turtle ,Screen
# import turtle
# import random
#
# cores = ["DodgerBlue3","firebrick1","gold","gold4","green","hotpink","khaki2","LightSalmon","BlueViolet","brown4"]
# direcoes = [0,90,180,270, 45, 135, 225, 315]
#
# seta = turtle.Turtle()
# seta.shape("arrow")
# seta.speed(8)
# seta.pensize(2)
# turtle.colormode(255)
#
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tuple = (r, g, b)
#     return tuple
#
# for i in range(1,250):
#     seta.forward(random.choice(range(20,50)))
#     seta.color(random_color())
#     seta.setheading(random.choice(range(0,359)))
#
# myscreen = Screen()
# myscreen.exitonclick()


####### HOTKEY CONTROL ###################

from turtle import Turtle, Screen
import turtle


cores = ["DodgerBlue3","firebrick1","gold","gold4","green","hotpink","khaki2","LightSalmon","BlueViolet","brown4"]
direcoes = [0, 90, 180, 270, 45, 135, 225, 315]

seta = turtle.Turtle()
seta.shape("arrow")
seta.speed(9)
seta.pensize(2)
turtle.colormode(255)



def move_forward():
    seta.forward(10)

def move_backward():
    seta.backward(10)

def turn_left():
    seta.left(20)

def turn_right():
    seta.right(20)


myscreen = Screen()
myscreen.listen()
myscreen.onkey(move_forward,key="w")
myscreen.onkey(move_backward,key="s")
myscreen.onkey(turn_left,key="a")
myscreen.onkey(turn_right,key="d")
myscreen.exitonclick()






