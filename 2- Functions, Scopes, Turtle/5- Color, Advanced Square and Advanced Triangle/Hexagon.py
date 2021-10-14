import turtle

turtle.shape("turtle")
turtle.speed(10)

turtle.pencolor("blue")
turtle.width(2)

for i in range(6):
  turtle.left(60)

  turtle.forward(50)
  turtle.left(120)
  turtle.forward(50)
  turtle.left(120)
  turtle.forward(50)
  turtle.left(120)

turtle.exitonclick()