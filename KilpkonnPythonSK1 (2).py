#Sander Kulma
#IT20
#12.01.2021
#Kilpkonn

import turtle

kilp1 = turtle.Turtle()
kilp1.color("green")
kilp1.fd(100)

kilp2 = turtle.Turtle()
kilp2.color("red")
kilp2.right(90)
kilp2.forward(100)

kilp3 = turtle.Turtle()
kilp3.color("yellow")
kilp3.left(90)
kilp3.forward(100)

kilp4 = turtle.Turtle()
kilp4.color("blue")
kilp4.left(180)
kilp4.forward(100)

kilp5 = turtle.Turtle()
kilp5.color("red")
kilp5.left(45)
kilp5.forward(100)

kilp6 = turtle.Turtle()
kilp6.color("orange")
kilp6.right(45)
kilp6.forward(100)

kilp7 = turtle.Turtle()
kilp7.color("green")
kilp7.right(140)
kilp7.forward(100)

kilp8 = turtle.Turtle()
kilp8.color("blue")
kilp8.left(140)
kilp8.forward(100)



input()
#ekraan
a = turtle.Screen()
a.setup(300,300)
a.bgcolor("yellow")
a.title("Kilpkonna harjutused")

k1 = turtle.Turtle()
k1.color("red")
k1.forward(100)
k1.left(90)
k1.forward(100)
k1.lt(90)
k1.fd(100)

k2 = turtle.Turtle()
k2.color("green")
k2.fd(100)
k2.rt(90)
k2.fd(100)
k2.rt(90)
k2.fd(100)


turtle.exitonclick()