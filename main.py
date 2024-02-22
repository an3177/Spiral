"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
class shapes:
  shape = turtle.Turtle()
  shape.speed(0)
  colors = ["blue", "red", "yellow", "green", "purple", "orange",]
  def triangle(len,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for i in range(3):
      shapes.shape.fd(len)
      shapes.shape.left(120)
  def square(len,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for i in range(4):
      shapes.shape.fd(len)
      shapes.shape.left(90)
  def spiral(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for i in range(r):
      for c in range(180):
        shapes.shape.fd(0.5+(i/2))
        shapes.shape.lt(1)
        shapes.shape.color(shapes.colors[c%6])
  def spiral2(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for c in range(r):
      shapes.shape.fd(c)
      shapes.shape.lt(125)
      shapes.square(c,x,y)
      shapes.shape.color(shapes.colors[c%6])
  def spiral3(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for c in range(r):
      shapes.shape.fd(c)
      shapes.shape.lt(125)
      shapes.shape.color(shapes.colors[c%6])
  def spiral4(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for c in range(r):
      shapes.shape.fd(c)
      shapes.shape.lt(120)
      shapes.shape.color(shapes.colors[c%6])
  def spiral5(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for c in range(r):
      shapes.shape.fd(c)
      shapes.shape.lt(120)
      shapes.triangle(c,x,y)
      shapes.shape.color(shapes.colors[c%6])
  def spiral6(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for c in range(r):
      shapes.shape.fd(c)
      shapes.shape.lt(175)
      shapes.square(c,x,y)
      shapes.shape.color(shapes.colors[c%6])
  def spiral7(r,x,y):
    shapes.shape.pu()
    shapes.shape.goto(x,y)
    shapes.shape.pd()
    for c in range(r):
      shapes.shape.fd(c)
      shapes.shape.lt(170)
      shapes.square(c,x,y)
      shapes.shape.color(shapes.colors[c%6])
  

shapes.spiral(20,0,0)
shapes.spiral2(500,0,0)
shapes.spiral7(600,0,0)