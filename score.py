from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.points_1 = 0
        self.points_2 = 0


    def scoreboard_1(self):
        self.goto(50, 230)
        self.clear()
        self.write(f"{self.points_1}", align="center", font=("Gourmand", 32, "normal"))

    def scoreboard_2(self):
        self.goto(-50, 230)
        self.clear()
        self.write(f"{self.points_2}", align="center", font=("Gourmand", 32, "normal"))

    def win_1(self):
        self.goto(0, 0)
        self.color("yellow")
        self.clear()
        self.write("RIGHT PLAYER WIN!", align="center", font=("Gourmand", 32, "normal"))

    def win_2(self):
        self.goto(0, 0)
        self.color("yellow")
        self.clear()
        self.write("LEFT PLAYER WIN!", align="center", font=("Gourmand", 32, "normal"))
