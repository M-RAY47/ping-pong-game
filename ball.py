from turtle import Turtle
import random

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.move(0,0)
		self.bounce()

	def move(self, x_cor, y_cor):
		x_cor +=1
		y_cor+=1 

	def bounce(self):
		self.fd(10)