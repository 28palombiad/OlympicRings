import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")

t = turtle.Turtle()

t.penup()
t.goto(-80,15)
t.pencolor("blue")
t.pendown()
t.circle(35)

t.penup()
t.goto(0,15)
t.pencolor("black")
t.pendown()
t.circle(35)


t.penup()
t.goto(80,15)
t.pencolor("red")
t.pendown()
t.circle(35)

t.penup()
t.goto(-40,-15)
t.pencolor("yellow")
t.pendown()
t.circle(35)

t.penup()
t.goto(40,-15)
t.pencolor("green")
t.pendown()
t.circle(35)

t.penup()
t.goto(0,100)
t.pencolor("purple")
t.pendown()
t.write("Winter Olympics",font=("Arial",40,"bold"),align="center")


t.penup()
t.goto(0,-100)
t.pencolor("purple")
t.pendown()
t.write("2026",font=("Arial",40,"bold"),align="center")


turtle.done()
