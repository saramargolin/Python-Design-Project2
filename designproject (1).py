#using functions
#Arsh
#main progarm
import turtle
from arshsfunction import *
turtle.colormode(255)
turtle.bgcolor('blue')

bob= turtle.Turtle()
bob.speed(3)
bob.pensize(1)
jump(bob,-9,11)

    
bob.pensize(1.5)
jump(bob,-16,130)
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,150)
    bob.right(160)
bob.penup()
bob.forward(136)
bob.pendown()
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,150)
    bob.right(160)
bob.penup()
bob.right(95)
bob.forward(35)
bob.pendown()
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,150)
    bob.right(160)
bob.penup()
bob.right(200)
bob.pendown()
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,160)
    bob.right(160)
bob.penup()
bob.right(92)
bob.forward(41)
bob.pendown()
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,160)
    bob.right(160)
bob.penup()
bob.left(154)
bob.forward(4)
bob.pendown()
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,160)
    bob.right(160)
bob.penup()
bob.left(268)
bob.forward(35)
bob.pendown()
for times in range(10):
    c=(230,2*times,31)
    bob.color(c)
    tree3(bob,153)
    bob.right(160)
bob.pensize(1.5)
jump(bob,-467,-75)
for times in range(30):
    c=(90+times,255,times+3)
    bob.color(c)
    tree4(bob,190)
    bob.right(220)
jump(bob,515,106)
for times in range(30):
    c=(90+times,255,times+3)
    bob.color(c)
    tree4(bob,190)
    bob.right(220)
    





