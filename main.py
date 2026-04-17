from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("It's PONG time")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeypress(r_paddle.start_down, "Down")

screen.onkeypress(l_paddle.start_up, "w")
screen.onkeypress(l_paddle.start_down, "s")

screen.onkeyrelease(r_paddle.stop, "Up")
screen.onkeyrelease(r_paddle.stop, "Down")

screen.onkeyrelease(l_paddle.stop, "w")
screen.onkeyrelease(l_paddle.stop, "s")

t = Turtle()
t.penup()
t.color("white")
t.goto(0,300)
t.setheading(270)
t.pensize(5)
for _ in range(15): # Repeat 10 times
    t.pendown()      # Put the pen down to draw
    t.forward(20)    # Draw a line 15 units long
    t.penup()        # Lift the pen up to stop drawing
    t.forward(20)    # Move 10 units to create a space


game_on = True
while game_on:
    r_paddle.move()
    l_paddle.move()

    time.sleep(ball.move_speed)
    ball.move_ball()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right missed the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reverse()

    # left missed the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reverse()


    screen.update()


screen.exitonclick()
