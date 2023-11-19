from turtle import Turtle, Screen

tim = Turtle()

#Turtle properties
tim.shape("turtle")
tim.color("red")

#Pen
tim.pendown()
tim.pensize(2)

for i in range(3,11):
    angle = 360 / i
    j = 0

    while j < i:
        tim.forward(100)
        tim.right(angle)
        j += 1





























screen = Screen()
screen.exitonclick()
