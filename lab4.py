# Unicode for empty box, u"\u25A0"
# Unicode for black box, u"\u25A1"
# can double check if Unicodes are true
from tkinter import *
import random
import math

w = u"\u25A0"

b = u"\u25A1"

SolvedBoard = ['u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"']

board = [
	b, b, b, b, b,
	b, b, b, b, b,
	b, b, b, b, b,
	b, b, b, b, b,
	b, b, b, b, b]

def Main():
	MakeBoard(board)
	global PuzzleSolve
	global cord
	global column
	play5()
	while PuzzleSolve == 0:
		display(board)
		userint()
		global cord
		play(row, column)
		global cord
		print(cord)
		play2()
		play4()
		play5()
	else:
		print("You have solved the puzzle!")
		
def MakeBoard(board):
	for i in range(len(board)):
		dec = random.random()
		if dec >= 0.5:  
			board[i] = b			
		else:
			board[i] = w

def display(board):
	print(board[0],board[1],board[2],board[3],board[4])
	print(board[5],board[6],board[7],board[8],board[9])
	print(board[10],board[11],board[12],board[13],board[14])
	print(board[15],board[16],board[17],board[18],board[19])
	print(board[20],board[21],board[22],board[23],board[24])

def play(row, column):
	global cord
	if row == 0 and column == 0:
		cord = 0
	elif row == 0 and column == 1:
		cord = 1
	elif row == 0 and column == 2:
		cord = 2
	elif row == 0 and column == 3:
		cord = 3
	elif row == 0 and column == 4:
		cord = 4
	elif row == 1 and column == 0:
		cord = 5
	elif row == 1 and column == 1:
		cord = 6
	elif row == 1 and column == 2:
		cord = 7
	elif row == 1 and column == 3:
		cord = 8
	elif row == 1 and column == 4:
		cord = 9
	elif row == 2 and column == 0:
		cord = 10
	elif row == 2 and column == 1:
		cord = 11
	elif row == 2 and column == 2:
		cord = 12
	elif row == 2 and column == 3:
		cord = 13
	elif row == 2 and column == 4:
		cord = 14
	elif row == 3 and column == 0:
		cord = 15
	elif row == 3 and column == 1:
		cord = 16
	elif row == 3 and column == 2:
		cord = 17
	elif row == 3 and column == 3:
		cord = 18
	elif row == 3 and column == 4:
		cord = 19
	elif row == 4 and column == 0:
		cord = 20
	elif row == 4 and column == 1:
		cord = 21
	elif row == 4 and column == 2:
		cord = 22
	elif row == 4 and column == 3:
		cord = 23
	elif row == 4 and column == 4:
		cord = 24
	return cord

def play2():
	global cord
	if cord == "b":
		board.pop(cord)
		board.insert(cord, "w")
	elif cord == "w":
		board.pop(cord)
		board.insert(cord, "b")

def play3():
	global cord
	if cord + 5 == "b":
		board.pop(cord + 5)
		board.insert(cord + 5, "w")
	if cord + 5 == "w":
		board.pop(cord + 5)
		board.insert(cord + 5, "b")
	if cord - 5 == "b":
		board.pop(cord - 5)
		board.insert(cord - 5, "w")
	if cord - 5 == "w":
		board.pop(cord - 5)
		board.insert(cord - 5, "b")
	if cord + 1 == "b":
		board.pop(cord + 1)
		board.pop(cord + 1, "w")
	if cord + 1 == "w":
		board.pop(cord + 1)
		board.insert(cord + 1, "b")
	if cord - 1 == "b":
		board.pop(cord - 1)
		board.insert(cord - 1, "w")
	if cord - 1 == "w":
		board.pop(cord - 1)
		board.insert(cord - 1, "b")
		play5()
#needs to be last play	
def play5():
	if board != SolvedBoard:
		global PuzzleSolve
		PuzzleSolve = 0

def play4():
	global cord
	if cord == 5 or cord == 10 or cord == 15:
		play6()
	else:
		play7()

def play6():
	global cord
	if cord + 5 == "b":
		board.pop(cord + 5)
		board.insert(cord + 5, "w")
	if cord + 5 == "w":
		board.pop(cord + 5)
		board.insert(cord + 5, "b")
	if cord - 5 == "b":
		board.pop(cord - 5)
		board.insert(cord - 5, "w")
	if cord - 5 == "w":
		board.pop(cord - 5)
		board.insert(cord - 5, "b")
	if cord + 1 == "b":
		board.pop(cord + 1)
		board.pop(cord + 1, "w")
	if cord + 1 == "w":
		board.pop(cord + 1)
		board.insert(cord + 1, "b")
		play5()

def play7():
	global cord
	if cord == 9 or cord == 14 or cord == 19:
		play8()
	else:
		play9()

def play8():
	global cord
	if cord + 5 == "b":
		board.pop(cord + 5)
		board.insert(cord + 5, "w")
	if cord + 5 == "w":
		board.pop(cord + 5)
		board.insert(cord + 5, "b")
	if cord - 5 == "b":
		board.pop(cord - 5)
		board.insert(cord - 5, "w")
	if cord - 5 == "w":
		board.pop(cord - 5)
		board.insert(cord - 5, "b")
	if cord - 1 == "b":
		board.pop(cord - 1)
		board.insert(cord - 1, "w")
	if cord - 1 == "w":
		board.pop(cord - 1)
		board.insert(cord - 1, "b")
		play5()

def play9():
	global cord
	if cord == 1 or cord == 2 or cord == 3:
		play10()
	else:
		play11()

def play10():
	global cord
	if cord + 5 == "b":
		board.pop(cord + 5)
		board.insert(cord + 5, "w")
	if cord + 5 == "w":
		board.pop(cord + 5)
		board.insert(cord + 5, "b")
	if cord + 1 == "b":
		board.pop(cord + 1)
		board.pop(cord + 1, "w")
	if cord + 1 == "w":
		board.pop(cord + 1)
		board.insert(cord + 1, "b")
	if cord - 1 == "b":
		board.pop(cord - 1)
		board.insert(cord - 1, "w")
	if cord - 1 == "w":
		board.pop(cord - 1)
		board.insert(cord - 1, "b")
		play5()

def play11():
	global cord
	if cord == 21 or cord == 22 or cord == 23:
		play12()
	else:
		play13()

def play12():
	global cord
	if cord - 5 == "b":
		board.pop(cord - 5)
		board.insert(cord - 5, "w")
	if cord - 5 == "w":
		board.pop(cord - 5)
		board.insert(cord - 5, "b")
	if cord + 1 == "b":
		board.pop(cord + 1)
		board.pop(cord + 1, "w")
	if cord + 1 == "w":
		board.pop(cord + 1)
		board.insert(cord + 1, "b")
	if cord - 1 == "b":
		board.pop(cord - 1)
		board.insert(cord - 1, "w")
	if cord - 1 == "w":
		board.pop(cord - 1)
		board.insert(cord - 1, "b")
		play5()

def play13():
	global cord
	if cord == 0:
		play14()
	else:
		play15()

def play14():
	global cord
	if cord + 5 == "b":
		board.pop(cord + 5)
		board.insert(cord + 5, "w")
	if cord + 5 == "w":
		board.pop(cord + 5)
		board.insert(cord + 5, "b")
	if cord + 1 == "b":
		board.pop(cord + 1)
		board.pop(cord + 1, "w")
	if cord + 1 == "w":
		board.pop(cord + 1)
		board.insert(cord + 1, "b")
		play5()

def play15():
	global cord
	if cord == 4:
		play16()
	else:
		play17()

def play16():
	global cord
	if cord + 5 == "b":
		board.pop(cord + 5)
		board.insert(cord + 5, "w")
	if cord + 5 == "w":
		board.pop(cord + 5)
		board.insert(cord + 5, "b")
	if cord - 1 == "b":
		board.pop(cord - 1)
		board.insert(cord - 1, "w")
	if cord - 1 == "w":
		board.pop(cord - 1)
		board.insert(cord - 1, "b")
		play5()

def play17():
	global cord
	if cord == 20:
		play18()
	else:
		play19()

def play18():
	global cord
	if cord - 5 == "b":
		board.pop(cord - 5)
		board.insert(cord - 5, "w")
	if cord - 5 == "w":
		board.pop(cord - 5)
		board.insert(cord - 5, "b")
	if cord + 1 == "b":
		board.pop(cord + 1)
		board.pop(cord + 1, "w")
	if cord + 1 == "w":
		board.pop(cord + 1)
		board.insert(cord + 1, "b")
		play5()

def play19():
	global cord
	if cord == 24:
		play20()
	else:
		play3()

def play20():
	global cord
	if cord - 5 == "b":
		board.pop(cord - 5)
		board.insert(cord - 5, "w")
	if cord - 5 == "w":
		board.pop(cord - 5)
		board.insert(cord - 5, "b")
	if cord - 1 == "b":
		board.pop(cord - 1)
		board.insert(cord - 1, "w")
	if cord - 1 == "w":
		board.pop(cord - 1)
		board.insert(cord - 1, "b")
		play5()

def userint():
	print("welcome to 'Lights Out!'")
	print("Type the row you would like to select from 0 to 4")
	print("Example: 1")
	print("Then press 'ENTER' to continue")
	global row
	row = input()
	print("Type the column you would like to select from 0 to 4")
	print("Example: 1")
	print("Then press 'ENTER' to continue")
	global column
	column = input()

Main()
