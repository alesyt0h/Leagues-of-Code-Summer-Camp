import turtle

turtle.shape("turtle")
turtle.speed(1)

turtle.pencolor("blue")

for i in range(3):
  turtle.left(120)

  turtle.forward(50)
  turtle.left(120)
  turtle.forward(50)
  turtle.left(120)
  turtle.forward(50)
  turtle.left(120)

turtle.exitonclick()