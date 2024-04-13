"""
Created 2023-02-23
@author minh_nguyen
"""
import random
from turtle import Turtle, Screen
import ctypes

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('#bc6c25')
usr_bet = screen.textinput('Make your bet', 'Which turtle will win? Enter your choice')
colors = ['red', 'green', 'yellow', 'purple', 'blue', 'brown']
y_coordinate = [25, 75, 125, -25, -75, -125]
is_game_on = True
turtles = []
message = ''
winner = None

if usr_bet:
    for i in range(0,6):
        tt = Turtle(shape='turtle')
        tt.color(colors[i])
        tt.penup()
        tt.goto(-230, y_coordinate[i])
        turtles.append(tt)

    while is_game_on:
        for tur in turtles:
            distance = random.randint(1, 10)
            tur.forward(distance)
            if tur.xcor() > 225:
                is_game_on = False
                winner = tur
    if usr_bet == colors[turtles.index(winner)]:
        message = f"You got it, {usr_bet} turtle won!"
    else:
        message = f"You loose, {colors[turtles.index(winner)]} turtle won!"

    ctypes.windll.user32.MessageBoxW(0, message, "Result", 1)

screen.exitonclick()
