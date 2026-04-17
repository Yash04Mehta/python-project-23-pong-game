from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

        self.move_direction = 0

    def move(self):
        new_y = self.ycor() + self.move_direction * 20

        if -250 < new_y < 250:
            self.goto(self.xcor(), new_y)

    def start_up(self):
        self.move_direction = 1

    def start_down(self):
        self.move_direction = -1

    def stop(self):
        self.move_direction = 0