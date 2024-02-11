
import turtle
import colorsys
t=turtle.Turtle()
t.speed(60)
turtle.Screen().bgcolor('black')
n=36
h=0
for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.color(c)
    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)

turtle.done()

