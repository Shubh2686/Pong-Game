from turtle import Turtle
from score import Score


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move()
        self.collision_detect()
        self.bounce()

    def collision_detect(self):
        if self.xcor() > 380:
            Score().points_2 += 1
            return 1
            # self.x *= -1
        elif self.xcor() < -380:
            Score().points_1 += 1
            return 2


    def bounce(self):
        if self.ycor() >= 280:
            self.y *= -1
            # return True
        elif self.ycor() <= -279:
            self.y *= -1
            # return True

    def move(self):
        if -380 <= self.xcor() <= 380:
            self.goto(self.xcor() + self.x, self.ycor())
        # elif -380 <= self.xcor() <= 380 and self.x == 1:
        #     self.goto(self.xcor()-10, self.ycor())
        if -280 <= self.ycor() <= 280:
            self.goto(self.xcor(), self.ycor() + self.y)
        # elif -280 <= self.ycor() <= 280 and self.y == 1:
        #     self.goto(self.xcor(), self.ycor() - 10)
