
# Graphic using python

In this project, you can do a Graphic start design. To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
  pip install turtle
  pip install colorsys

```
    
## Deployment Project main.py

To deploy this project run

```bash
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
```

## Output 

![output](https://user-images.githubusercontent.com/123636419/215391010-9fc558a2-8f0e-485e-9d09-8e22118e8c91.PNG)

## Deployment Project main01.py

To deploy this project run

```bash
import turtle as t

t.bgcolor("black")
t.speed(0)
t.hideturtle()

colors = ["yellow", "red", "yellow", "red"]

for i in range(120):
    for c in colors:
        t.color(c)
        t.circle(200-i,100)
        t.lt(90)
        t.circle(200-i,100)
        t.rt(60)
        t.end_fill()
t.mainloop()
```
## Output 

![Output2](https://user-images.githubusercontent.com/123636419/216633117-5b39ec9d-30bd-45fe-b05b-cc1b083ccce1.PNG)



You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

If you have any confusion, please feel free to contact me. Thank you

