import turtle

mypen=turtle.Turtle()
mypen.pensize(5)

mypen.color("blue")
mypen.penup()
mypen.goto(-110,-25)
mypen.pendown()
mypen.circle(45)

mypen.color("black")
mypen.penup()
mypen.goto(0,-25)
mypen.pendown()
mypen.circle(45)

mypen.color("red")
mypen.penup()
mypen.goto(110,-25)
mypen.pendown()
mypen.circle(45)

mypen.color("yellow")
mypen.penup()
mypen.goto(-55,-75)
mypen.pendown()
mypen.circle(45)

mypen.color("green")
mypen.penup()
mypen.goto(55,-75)
mypen.pendown()
mypen.circle(45)
