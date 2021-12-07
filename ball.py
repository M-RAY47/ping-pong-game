from turtle import Turtle
import random

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.mv_speed = 0.1
		self.move()
		self.bounce_y()

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1
		self.mv_speed *= 0.9

	def bounce_x(self):
		self.x_move *= -1

	def res_position(self):
		self.goto(0,0)
		self.mv_speed = 0.9
		self.bounce_x