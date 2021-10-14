import turtle

turtle.shape("turtle")
turtle.speed(10)

turtle.pencolor("blue")
turtle.width(2)

for i in range(30):
  turtle.forward(10 * i)
  turtle.left(90)
  turtle.forward(10 * i)
  turtle.left(90)

turtle.exitonclick()

# Weird Pyramid (Cool)
#
# for i in range(100):
# #   turtle.left(60)

#   turtle.forward(5 * i)
#   turtle.left(90)
#   turtle.forward(5 * i)
#   turtle.left(90)
#   turtle.forward(5 * i)
#   turtle.left(90)