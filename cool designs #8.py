import turtle
import colorsys
t=turtle.Turtle()
turtle.Screen().bgcolor('black')
t.penup()
t.goto(-200,-100)
t.pendown()
t.speed(0)
a=400
h=0
n=100
def obj():
    global a,n,h
    for i in range(40):
        c=colorsys.hsv_to_rgb(h,1,0.6)
        h=h+(1/n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a=a-10

obj()
obj()
t.hideturtle()
turtle.done()