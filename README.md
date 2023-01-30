
# Graphic using python

In this project, you can do a Graphic start design. To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
  pip install turtle
  pip install colorsys

```
    
## Deployment

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


![output](https://user-images.githubusercontent.com/123636419/215391010-9fc558a2-8f0e-485e-9d09-8e22118e8c91.PNG)


