from turtle import *
import colorsys


tracer(10)
bgcolor('black')
pensize(4)

h = 0

for i in range(411):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 1/37
    begin_fill()
    fillcolor('black')
    left(120)
    forward(i)
    left(3)
    circle(i,12)
    end_fill()

done()


