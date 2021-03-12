from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
tim = Turtle()
tim.shape("square")
tim.turtlesize(stretch_wid=30, stretch_len=0.5)
tim.color("white")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect with collision of wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect of wall paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect the R misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect the L misses
    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

