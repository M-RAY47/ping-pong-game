import tkinter as TK
from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball

time.sleep(0.1)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
rd_paddle = Paddle((380, 0))
lt_paddle = Paddle((-380,0))
# display  ball on the screen
ball =Ball()

game_is_on= True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	ball.move()

	#Collision with the Screen
	if ball.y_cor() > 280 or ball.y_cor() < -280:
		ball.bounce_y()

	#Detection of collision with the Paddle
	if ball.distance(rd_paddle) < 50 and ball.xcor() > 320 or ball.distance(lt_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	# When the right paddle misses the ball, the ball
	if ball.xcor() > 380:
		ball.res_position()

	# When the left paddle misses the ball, the ball
	if ball.xcor() > 380:
		ball.res_position()

screen.exitonclick()