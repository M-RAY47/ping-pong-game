from turtle import Turtle

class Pawn(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.penup()
		self.shapesize(stretch_wid=5,stretch_len=1)