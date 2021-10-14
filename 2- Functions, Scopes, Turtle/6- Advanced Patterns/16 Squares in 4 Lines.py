import turtle

turtle.shape("turtle")
turtle.color("blue")
turtle.speed(10)
turtle.width(2)

for i in range(4):
    for a in range(4):
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.penup()
        turtle.forward(35)
        turtle.pendown()
    turtle.penup()
    turtle.backward(140)
    turtle.right(90)
    turtle.forward(35)
    turtle.left(90)
    turtle.pendown()

turtle.exitonclick()