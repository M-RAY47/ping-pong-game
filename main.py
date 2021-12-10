# import tkinter as TK
from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

time.sleep(0.1)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
rd_paddle = Paddle((350, 0))
lt_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(rd_paddle.go_up, "Up")
screen.onkey(rd_paddle.go_down, "Down")
screen.onkey(lt_paddle.go_up, "w")
screen.onkey(lt_paddle.go_down, "s")

# display  ball on the screen
ball =Ball()
#show the scoreboard on the screen
scoreboard = Scoreboard()

game_is_on= True
while game_is_on:
	screen.update()
	time.sleep(ball.mv_speed)
	ball.move()

	#Collision with the Screen
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	#Detection of collision with the Paddle
	if ball.distance(rd_paddle) < 50 and ball.xcor() > 320 or ball.distance(lt_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	# When the right paddle misses the ball, the ball
	if ball.xcor() > 380:
		ball.res_position()
		scoreboard.lt_point()

	# When the left paddle misses the ball, the ball
	if ball.xcor() < -380:
		ball.res_position()
		scoreboard.rd_point()

screen.exitonclick()