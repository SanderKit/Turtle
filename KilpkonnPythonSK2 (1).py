#Sander Kulma
#IT20
#12.01.2021
#Kilpkonn
#Harjutus 2

import turtle
import random

#Kolmnurk
def kolmnurk(a,b):
    kk = turtle.Turtle()
    nurk = 120
    kk.color(b)
    for i in range(3):
        kk.fd(a)
        kk.lt(nurk)

k = int(input("Kylje pikkus: "))
v = input("Lisa v2rv, (red, green, blue): ")
kolmnurk(k,v)

input()
#Aken
screen = turtle.Screen()
screen.setup(300,300)

#Creating the structure
def viisnurk():
    corner = -144
    k = turtle.Turtle()
    for i in range(5):
        k.fd(100)
        k.lt(corner)
    
viisnurk()
turtle.exitonclick()
    

