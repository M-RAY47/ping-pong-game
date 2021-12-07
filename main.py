import tkinter as TK
from turtle import Screen, Turtle
from pawn import Pawn
import time
from ball import Ball

time.sleep(0.1)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
rd_pawn = Pawn()
lt_pawn = Pawn()
rd_pawn.goto(380, 0)
lt_pawn.goto(-380,0)
ball =Ball()

game_is_on= True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	ball.move()


screen.exitonclick()