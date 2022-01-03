from turtle import Turtle


class Slider(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(position)
        self.s1_up()
        self.s2_up()
        self.s1_down()
        self.s2_down()

    def s1_up(self):
        if self.ycor() != 250:
            self.forward(50)

    def s2_up(self):
        if self.ycor() != 250:
            self.forward(50)

    def s1_down(self):
        if self.ycor() != -250:
            self.backward(50)

    def s2_down(self):
        if self.ycor() != -250:
            self.backward(50)
