import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(3)

# Base
pen.penup()
pen.goto(-150, -100)
pen.pendown()
pen.color("black", "white")
pen.begin_fill()
for _ in range(2):
    pen.forward(300)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
pen.end_fill()

# Dome
pen.penup()
pen.goto(0, 50)
pen.pendown()
pen.color("black", "white")
pen.begin_fill()
pen.circle(60)
pen.end_fill()

# Left Minar
pen.penup()
pen.goto(-130, -100)
pen.pendown()
pen.left(90)
pen.forward(200)

# Right Minar
pen.penup()
pen.goto(130, -100)
pen.pendown()
pen.forward(200)

turtle.done()
