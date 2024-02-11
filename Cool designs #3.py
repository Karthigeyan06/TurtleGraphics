import turtle
import colorsys
t=turtle.Turtle()
t.speed(50)
turtle.Screen().bgcolor('black')
n=36
h=0
for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.left(145)
    for i in range(5):
        t.circle(35*i)
        t.circle(-35*i)
        t.left(i)
turtle.done()