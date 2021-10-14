import turtle

turtle.shape("arrow")

for i in range(10):
  turtle.forward(10 + (i*2))
  turtle.penup()
  turtle.forward(5)
  turtle.pendown()

turtle.exitonclick()