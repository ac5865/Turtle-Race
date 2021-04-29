from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["orange", "purple", "green", "yellow", "red", "blue"]
y_axis = [-100, -60, -20, 20, 60, 100]

all_turtle = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_axis[i])
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
if user_bet:
    is_race_on=True
    while is_race_on:
        for turtle in all_turtle:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    print("You have won!")
                else:
                    print("You lose" + winning_color + "wins")
            ran_dist = random.randint(0, 10)
            turtle.forward(random.randint(0, 10))
screen.exitonclick()
