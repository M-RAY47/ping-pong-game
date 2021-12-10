from turtle import Turtle

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.lt_score = 0
		self.rd_score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-100, 200)
		self.write(self.lt_score, align="center", font=("Courier", 80, "normal"))
		self.goto(100, 200)
		self.write(self.rd_score, align="center", font=("Courier", 80, "normal"))
	
	def lt_point(self):
		print("Before:",self.lt_score)
		self.lt_score += 1
		print("After:",self.lt_score)
		self.update_scoreboard()
		# print("AFTER Update:",self.update_scoreboard)
	
	def rd_point(self):
		self.clear()
		print("before:",self.rd_score)
		self.rd_score += 1
		print("After:",self.rd_score)
		self.clear()
		self.update_scoreboard()