import turtle

turtle.shape("turtle")
turtle.color("blue")
turtle.speed(10)
turtle.width(2)

for i in range(5):

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

turtle.exitonclick()