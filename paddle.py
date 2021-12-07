from turtle import Turtle

class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.penup()
		self.shapesize(stretch_wid=5,stretch_len=1)
		self.goto(position)
		
	def go_up(self):
		new_y = self.y_cor() + 20
		self.goto(self.x_cor(), new_y)

	def go_down(self):
		new_y = self.y_cor() - 20
		self.goto(self.x_cor(), new_y)