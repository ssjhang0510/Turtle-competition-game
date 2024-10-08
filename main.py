from turtle import Turtle, Screen
import random
# tim = Turtle()
screen = Screen()


# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def clockwise():
#     tim.right(10)
#
#
# def counter_clockwise():
#     tim.left(10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="c", fun=clear)

#  ------------------------------------------------------------------------------

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:"
                                                          "[red, orange, yellow, green, blue, purple]")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

# another methods
# def turtles(x, y, c):
#     tim = Turtle(shape="turtle")
#     tim.color(colors[c])
#     tim.penup()
#     tim.goto(x, y)
#
#
# turtles(-230, 140, 0)
# turtles(-230, 80, 1)
# turtles(-230, 20, 2)
# turtles(-230, -40, 3)
# turtles(-230, -100, 4)
# turtles(-230, -160, 5)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
