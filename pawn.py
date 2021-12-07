from turtle import Turtle

class Pawn(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.penup()
		self.shapesize(stretch_wid=5,stretch_len=1)
	def go_up(self):
		new_y = self.y_cor() + 20
		self.goto(self.x_cor() + new_y)