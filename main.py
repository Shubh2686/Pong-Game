from turtle import Screen
from slider import Slider
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

slider_1 = Slider((350, 0))
slider_2 = Slider((-350, 0))
seperation = Slider((0, 0))
seperation.shapesize(stretch_wid=1, stretch_len=30)
seperation.color("red")
ball = Ball()
score1 = Score()
score2 = Score()


screen.listen()
screen.onkey(fun=slider_1.s1_up, key="Up")
screen.onkey(fun=slider_2.s2_up, key="w")
screen.onkey(fun=slider_1.s1_down, key="Down")
screen.onkey(fun=slider_2.s2_down, key="s")

while score1.points_1 < 3 and score2.points_2 < 3:
    t = 0.1
    time.sleep(0.5)
    ball.goto(0, 0)
    ball.bounce()
    is_game_on = True
    while is_game_on:
        if ball.collision_detect() == 1:
            score2.points_2 += 1
            ball.x *= -1
            is_game_on = False
        if ball.collision_detect() == 2:
            score1.points_1 += 1
            ball.x *= -1
            is_game_on = False
        score1.scoreboard_1()
        score2.scoreboard_2()
        screen.update()
        ball.move()
        ball.bounce()
        if 320 < ball.xcor() < 350 and 0 < slider_1.distance(ball) < 60:
            t *= 0.9
            ball.x *= -1
        elif -350 < ball.xcor() < -320 and 0 < slider_2.distance(ball) < 60:
            t *= 0.9
            ball.x *= -1

        time.sleep(t)
    if score1.points_1 == 3:
        Score().win_1()
    elif score2.points_2 == 3:
        Score().win_2()

screen.exitonclick()
