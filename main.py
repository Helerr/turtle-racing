import turtle as t
import random

screen = t.Screen()

screen.setup(width=500, height=400)
screen.title("Turtle RACING!")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-120, -80, -40, 0, 40, 80, 120]
turtle_racers = []
is_race_on = False
has_won = False

for _ in range(len(colors)):
    turtle_racers.append(t.Turtle(shape="turtle"))
    turtle_racers[_].color(colors[_])
    turtle_racers[_].penup()
    turtle_racers[_].goto(x=-230, y=y_position[_])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_index in range(len(turtle_racers)):
        if turtle_racers[turtle_index].xcor() > 230:
            if turtle_racers[turtle_index].color()[0] == user_bet.lower():
                screen.clear()
                print(f"{user_bet.capitalize()} has won! Congratulations!")
                turtle_racers[turtle_index].home()
                turtle_racers[turtle_index].hideturtle()
                turtle_racers[turtle_index].write("Congratulations! Your turtle won!", move=False, align="center",
                                                  font=('Arial', 16, 'normal'))
                is_race_on = False
            else:
                screen.clear()
                print("Your turtle has lost!")
                turtle_racers[turtle_index].home()
                turtle_racers[turtle_index].hideturtle()
                turtle_racers[turtle_index].write(
                    f"{turtle_racers[turtle_index].color()[0].capitalize()} has won. Better luck next time.",
                    move=False,
                    align="center",
                    font=('Arial', 16, 'normal'))
                is_race_on = False
        random_distance = random.randint(0, 10)
        turtle_racers[turtle_index].forward(random_distance)
        position_tuple = (230, y_position[turtle_index])

screen.exitonclick()
