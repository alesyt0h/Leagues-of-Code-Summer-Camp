import turtle

turtle.shape("turtle")

for i in range(10):
  turtle.forward(10)
  turtle.penup()
  turtle.backward(10)
  turtle.right(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.pendown()

turtle.exitonclick()