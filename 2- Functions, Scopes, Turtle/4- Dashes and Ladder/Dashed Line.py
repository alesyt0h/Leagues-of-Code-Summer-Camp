import turtle

turtle.shape("arrow")

for i in range(10):
  turtle.forward(15)
  turtle.penup()
  turtle.forward(5)
  turtle.pendown()
  # turtle.forward(10)
  # turtle.penup()
  # turtle.forward(3)
  # turtle.pendown()

turtle.exitonclick()