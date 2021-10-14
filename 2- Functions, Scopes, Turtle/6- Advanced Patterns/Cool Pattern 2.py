import turtle

turtle.shape("turtle")
turtle.speed(20)


sides = 3

for x in range(200):
  turtle.left(360 / sides + 10)
  turtle.forward(x * 6 / sides + x)
  turtle.width(x * sides / 200)

turtle.exitonclick()