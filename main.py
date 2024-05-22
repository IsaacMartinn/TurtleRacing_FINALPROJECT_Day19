from turtle import Turtle, Screen
import random

def turtle_racing_game():
    is_race_on = False

    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle (red, orange, yellow, blue or purple) "
                                                              "will win the race?")
    colors = ["red", "orange", "yellow", "blue", "purple"]

    y_coor = -100

    all_turtes = []

    for turtle_index in range(0, 5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-240, y=y_coor)
        y_coor += 50
        all_turtes.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtes:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner")
            random_distance = random.randint(0, 10)
            turtle.fd(random_distance)

    screen.exitonclick()

turtle_racing_game()