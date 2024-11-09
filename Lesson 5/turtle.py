import turtle

turtle.shape("turtle")
turtle.speed(10)
turtle.color("black")

for i in range(50):
    turtle.circle(3 * i)
    turtle.left(30)