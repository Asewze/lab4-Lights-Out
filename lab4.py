# Unicode for empty box, u"\u25A0"
# Unicode for black box, u"\u25A1"
# can double check if Unicodes are true
from tkinter import *
import random
import math

w = u"\u25A0"

b = u"\u25A1"

SolvedBoard = ['u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"','u"\u25A1"']

global board

board = [
	b, b, b, b, b,
	b, b, b, b, b,
	b, b, b, b, b,
	b, b, b, b, b,
	b, b, b, b, b]

PuzzleSolve = 0

def Main():
	print("Welcome to 'Lights Out'")
	print("Try to turn all the lights off!")
	MakeBoard(board)
	global PuzzleSolve
	while PuzzleSolve == 0:
		display(board)
		userint()
		play(row, column)
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
	if row == '0' and column == '0':
		if board[0] == b:
			board.pop(0)
			board.insert(0, w)
			if board[5] == b:
				board.pop(5)
				board.insert(5, w)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					play5()
				else:
					board.pop(1)
					board.insert(1, b)
					play5()
			else:
				board.pop(5)
				board.insert(5, b)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					play5()
				else:
					board.pop(1)
					board.insert(1, b)
					play5()
		else:
			board.pop(0)
			board.insert(0, b)
			if board[5] == b:
				board.pop(5)
				board.insert(5, w)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					play5()
				else:
					board.pop(1)
					board.insert(1, b)
					play5()
			else:
				board.pop(5)
				board.insert(5, b)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					play5()
				else:
					board.pop(1)
					board.insert(1, b)
					play5()
	elif row == '0' and column == '1':
		if board[1] == b:
			board.pop(1)
			board.insert(1, w)
			if board[6] == b:
				board.pop(6)
				board.insert(6, w)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
			else:
				board.pop(6)
				board.insert(6, b)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
		else:
			board.pop(1)
			board.insert(1, b)
			if board[6] == b:
				board.pop(6)
				board.insert(6, w)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
			else:
				board.pop(6)
				board.insert(6, b)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
	elif row == '0' and column == '2':
		if board[2] == b:
			board.pop(2)
			board.insert(2, w)
			if board[7] == b:
				board.pop(7)
				board.insert(7, w)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
			else:
				board.pop(7)
				board.insert(7, b)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
		else:
			board.pop(2)
			board.insert(2, b)
			if board[7] == b:
				board.pop(7)
				board.insert(7, w)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
			else:
				board.pop(7)
				board.insert(7, b)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[1] == b:
						board.pop(1)
						board.insert(1, w)
						play5()
					else:
						board.pop(1)
						board.insert(1, b)
						play5()
	elif row == '0' and column == '3':
		if board[3] == b:
			board.pop(3)
			board.insert(3, w)
			if board[8] == b:
				board.pop(8)
				board.insert(8, w)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
			else:
				board.pop(8)
				board.insert(8, b)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
		else:
			board.pop(3)
			board.insert(3, b)
			if board[8] == b:
				board.pop(8)
				board.insert(8, w)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
			else:
				board.pop(8)
				board.insert(8, b)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[2] == b:
						board.pop(2)
						board.insert(2, w)
						play5()
					else:
						board.pop(2)
						board.insert(2, b)
						play5()
	elif row == '0' and column == '4':
		if board[4] == b:
			board.pop(4)
			board.insert(4, w)
			if board[9] == b:
				board.pop(9)
				board.insert(9, w)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					play5()
				else:
					board.pop(3)
					board.insert(3, b)
					play5()
			else:
				board.pop(9)
				board.insert(9, b)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					play5()
				else:
					board.pop(3)
					board.insert(3, b)
					play5()
		else:
			board.pop(4)
			board.insert(4, b)
			if board[9] == b:
				board.pop(9)
				board.insert(9, w)
				if board[3] == b:
					board.pop(3)
					board.pop(3, w)
					play5()
				else:
					board.pop(3)
					board.insert(3, b)
					play5()
			else:
				board.pop(9)
				board.insert(9, b)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					play5()
				else:
					board.pop(3)
					board.insert(3, b)
					play5()
	elif row == '1' and column == '0':
		if board[5] == b:
			board.pop(5)
			board.insert(5, w)
			if board[6] == b:
				board.pop(6)
				board.insert(6, w)
				if board[10] == b:
					board.pop(10)
					board.insert(10, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(10)
					board.insert(10, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
			else:
				board.pop(6)
				board.insert(6, b)
				if board[10] == b:
					board.pop(10)
					board.insert(10, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(10)
					board.insert(10, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
		else:
			board.pop(5)
			board.insert(5, b)
			if board[6] == b:
				board.pop(6)
				board.insert(6, w)
				if board[10] == b:
					board.pop(10)
					board.insert(10, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(10)
					board.insert(10, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
			else:
				board.pop(6)
				board.insert(6, b)
				if board[10] == b:
					board.pop(10)
					board.insert(10, w)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
				else:
					board.pop(10)
					board.insert(10, b)
					if board[0] == b:
						board.pop(0)
						board.insert(0, w)
						play5()
					else:
						board.pop(0)
						board.insert(0, b)
						play5()
	elif row == '1' and column == '1':
		if board[6] == b:
			board.pop(6)
			board.insert(6, w)
			if board[11] == b:
				board.pop(11)
				board.insert(11, w)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
				else:
					board.pop(1)
					board.insert(1, b)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
			else:
				board.pop(11)
				board.insert(11, b)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
				else:
					board.pop(1)
					board.insert(1, b)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
		else:
			board.pop(6)
			board.insert(6, b)
			if board[11] == b:
				board.pop(11)
				board.insert(11, w)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
				else:
					board.pop(1)
					board.insert(1, b)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
			else:
				board.pop(11)
				board.insert(11, b)
				if board[1] == b:
					board.pop(1)
					board.insert(1, w)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
				else:
					board.pop(1)
					board.insert(1, b)
					if board[7] == b:
						board.pop(7)
						board.insert(7, w)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
					else:
						board.pop(7)
						board.insert(7, b)
						if board[5] == b:
							board.pop(5)
							board.insert(5, w)
							play5()
						else:
							board.pop(5)
							board.insert(5, b)
							play5()
	elif row == '1' and column == '2':
		if board[7] == b:
			board.pop(7)
			board.insert(7, w)
			if board[12] == b:
				board.pop(12)
				board.insert(12, w)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
			else:
				board.pop(12)
				board.insert(12, b)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
		else:
			board.pop(7)
			board.insert(7, b)
			if board[12] == b:
				board.pop(12)
				board.insert(12, w)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
			else:
				board.pop(12)
				board.insert(12, b)
				if board[2] == b:
					board.pop(2)
					board.insert(2, w)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
				else:
					board.pop(2)
					board.insert(2, b)
					if board[8] == b:
						board.pop(8)
						board.insert(8, w)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
					else:
						board.pop(8)
						board.insert(8, b)
						if board[6] == b:
							board.pop(6)
							board.insert(6, w)
							play5()
						else:
							board.pop(6)
							board.insert(6, b)
							play5()
	elif row == '1' and column == '3':
		if board[8] == b:
			board.pop(8)
			board.insert(8, w)
			if board[13] == b:
				board.pop(13)
				board.insert(13, w)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
			else:
				board.pop(13)
				board.insert(13, b)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
		else:
			board.pop(8)
			board.insert(8, b)
			if board[13] == b:
				board.pop(13)
				board.insert(13, w)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
			else:
				board.pop(13)
				board.insert(13, b)
				if board[3] == b:
					board.pop(3)
					board.insert(3, w)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
				else:
					board.pop(3)
					board.insert(3, b)
					if board[9] == b:
						board.pop(9)
						board.insert(9, w)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
					else:
						board.pop(9)
						board.insert(9, b)
						if board[7] == b:
							board.pop(7)
							board.insert(7, w)
							play5()
						else:
							board.pop(7)
							board.insert(7, b)
							play5()
	elif row == '1' and column == '4':
		if board[9] == b:
			board.pop(9)
			board.insert(9, w)
			if board[8] == b:
				board.pop(8)
				board.insert(8, w)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
			else:
				board.pop(8)
				board.insert(8, b)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
		else:
			board.pop(9)
			board.insert(9, b)
			if board[8] == b:
				board.pop(8)
				board.insert(8, w)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
			else:
				board.pop(8)
				board.insert(8, b)
				if board[4] == b:
					board.pop(4)
					board.insert(4, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
				else:
					board.pop(4)
					board.insert(4, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						play5()
					else:
						board.pop(14)
						board.insert(14, b)
						play5()
	elif row == '2' and column == '0':
		if board[10] == b:
			board.pop(10)
			board.insert(10, w)
			if board[11] == b:
				board.pop(11)
				board.insert(11, w)
				if board[15] == b:
					board.pop(15)
					board.insert(15, w)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
				else:
					board.pop(15)
					board.insert(15, b)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
			else:
				board.pop(11)
				board.insert(11, b)
				if board[15] == b:
					board.pop(15)
					board.insert(15, w)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
				else:
					board.pop(15)
					board.insert(15, b)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
		else:
			board.pop(10)
			board.insert(10, b)
			if board[11] == b:
				board.pop(11)
				board.insert(11, w)
				if board[15] == b:
					board.pop(15)
					board.insert(15, w)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
				else:
					board.pop(15)
					board.insert(15, b)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
			else:
				board.pop(11)
				board.insert(11, b)
				if board[15] == b:
					board.pop(15)
					board.insert(15, w)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
				else:
					board.pop(15)
					board.insert(15, b)
					if board[5] == b:
						board.pop(5)
						board.insert(5, w)
						play5()
					else:
						board.pop(5)
						board.insert(5, b)
						play5()
	elif row == '2' and column == '1':
		if board[11] == b:
			board.pop(11)
			board.insert(11, w)
			if board[16] == b:
				board.pop(16)
				board.insert(16, w)
				if board[6] == b:
					board.pop(6)
					board.insert(6, w)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
				else:
					board.pop(6)
					board.insert(6, b)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
			else:
				board.pop(16)
				board.insert(16, b)
				if board[6] == b:
					board.pop(6)
					board.insert(6, w)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
				else:
					board.pop(6)
					board.insert(6, b)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
		else:
			board.pop(11)
			board.insert(11, b)
			if board[16] == b:
				board.pop(16)
				board.insert(16, w)
				if board[6] == b:
					board.pop(6)
					board.insert(6, w)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
				else:
					board.pop(6)
					board.insert(6, b)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
			else:
				board.pop(16)
				board.insert(16, b)
				if board[6] == b:
					board.pop(6)
					board.insert(6, w)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
				else:
					board.pop(6)
					board.insert(6, b)
					if board[12] == b:
						board.pop(12)
						board.insert(12, w)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
					else:
						board.pop(12)
						board.insert(12, b)
						if board[10] == b:
							board.pop(10)
							board.insert(10, w)
							play5()
						else:
							board.pop(10)
							board.insert(10, b)
							play5()
	elif row == '2' and column == '2':
		if board[12] == b:
			board.pop(12)
			board.insert(12, w)
			if board[17] == b:
				board.pop(17)
				board.insert(17, w)
				if board[7] == b:
					board.pop(7)
					board.insert(7, w)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
				else:
					board.pop(7)
					board.insert(7, b)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
			else:
				board.pop(17)
				board.insert(17, b)
				if board[7] == b:
					board.pop(7)
					board.insert(7, w)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
				else:
					board.pop(7)
					board.insert(7, b)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
		else:
			board.pop(12)
			board.insert(12, b)
			if board[17] == b:
				board.pop(17)
				board.insert(17, w)
				if board[7] == b:
					board.pop(7)
					board.insert(7, w)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
				else:
					board.pop(7)
					board.insert(7, b)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
			else:
				board.pop(17)
				board.insert(17, b)
				if board[7] == b:
					board.pop(7)
					board.insert(7, w)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
				else:
					board.pop(7)
					board.insert(7, b)
					if board[13] == b:
						board.pop(13)
						board.insert(13, w)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
					else:
						board.pop(13)
						board.insert(13, b)
						if board[11] == b:
							board.pop(11)
							board.insert(11, w)
							play5()
						else:
							board.pop(11)
							board.insert(11, b)
							play5()
	elif row == '2' and column == '3':
		if board[13] == b:
			board.pop(13)
			board.insert(13, w)
			if board[18] == b:
				board.pop(18)
				board.insert(18, w)
				if board[8] == b:
					board.pop(8)
					board.insert(8, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
				else:
					board.pop(8)
					board.insert(8, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
			else:
				board.pop(18)
				board.insert(18, b)
				if board[8] == b:
					board.pop(8)
					board.insert(8, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
				else:
					board.pop(8)
					board.insert(8, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
		else:
			board.pop(13)
			board.insert(13, b)
			if board[18] == b:
				board.pop(18)
				board.insert(18, w)
				if board[8] == b:
					board.pop(8)
					board.insert(8, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
				else:
					board.pop(8)
					board.insert(8, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
			else:
				board.pop(18)
				board.insert(18, b)
				if board[8] == b:
					board.pop(8)
					board.insert(8, w)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
				else:
					board.pop(8)
					board.insert(8, b)
					if board[14] == b:
						board.pop(14)
						board.insert(14, w)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
					else:
						board.pop(14)
						board.insert(14, b)
						if board[12] == b:
							board.pop(12)
							board.insert(12, w)
							play5()
						else:
							board.pop(12)
							board.insert(12, b)
							play5()
	elif row == '2' and column == '4':
		if board[14] == b:
			board.pop(14)
			board.insert(14, w)
			if board[13] == b:
				board.pop(13)
				board.insert(13, w)
				if board[9] == b:
					board.pop(9)
					board.insert(9, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
				else:
					board.pop(9)
					board.insert(9, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
			else:
				board.pop(13)
				board.insert(13, b)
				if board[9] == b:
					board.pop(9)
					board.insert(9, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
				else:
					board.pop(9)
					board.insert(9, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
		else:
			board.pop(14)
			board.insert(14, b)
			if board[13] == b:
				board.pop(13)
				board.insert(13, w)
				if board[9] == b:
					board.pop(9)
					board.insert(9, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
				else:
					board.pop(9)
					board.insert(9, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
			else:
				board.pop(13)
				board.insert(13, b)
				if board[9] == b:
					board.pop(9)
					board.insert(9, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
				else:
					board.pop(9)
					board.insert(9, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						play5()
					else:
						board.pop(19)
						board.insert(19, b)
						play5()
	elif row == '3' and column == '0':
		if board[15] == b:
			board.pop(15)
			board.insert(15, w)
			if board[16] == b:
				board.pop(16)
				board.insert(16, w)
				if board[20] == b:
					board.pop(20)
					board.insert(20, w)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
				else:
					board.pop(20)
					board.insert(20, b)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
			else:
				board.pop(16)
				board.insert(16, b)
				if board[20] == b:
					board.pop(20)
					board.insert(20, w)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
				else:
					board.pop(20)
					board.insert(20, b)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
		else:
			board.pop(15)
			board.insert(15, b)
			if board[16] == b:
				board.pop(16)
				board.insert(16, w)
				if board[20] == b:
					board.pop(20)
					board.insert(20, w)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
				else:
					board.pop(20)
					board.insert(20, b)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
			else:
				board.pop(16)
				board.insert(16, b)
				if board[20] == b:
					board.pop(20)
					board.insert(10, w)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
				else:
					board.pop(20)
					board.insert(20, b)
					if board[10] == b:
						board.pop(10)
						board.insert(10, w)
						play5()
					else:
						board.pop(10)
						board.insert(10, b)
						play5()
	elif row == '3' and column == '1':
		if board[16] == b:
			board.pop(16)
			board.insert(16, w)
			if board[21] == b:
				board.pop(21)
				board.insert(21, w)
				if board[11] == b:
					board.pop(11)
					board.insert(11, w)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
				else:
					board.pop(11)
					board.insert(11, b)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
			else:
				board.pop(21)
				board.insert(21, b)
				if board[11] == b:
					board.pop(11)
					board.insert(11, w)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
				else:
					board.pop(11)
					board.insert(11, b)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
		else:
			board.pop(16)
			board.insert(16, b)
			if board[21] == b:
				board.pop(21)
				board.insert(21, w)
				if board[11] == b:
					board.pop(11)
					board.insert(11, w)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
				else:
					board.pop(11)
					board.insert(11, b)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
			else:
				board.pop(21)
				board.insert(21, b)
				if board[11] == b:
					board.pop(11)
					board.insert(11, w)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
				else:
					board.pop(11)
					board.insert(11, b)
					if board[17] == b:
						board.pop(17)
						board.insert(17, w)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
					else:
						board.pop(17)
						board.insert(17, b)
						if board[15] == b:
							board.pop(15)
							board.insert(15, w)
							play5()
						else:
							board.pop(15)
							board.insert(15, b)
							play5()
	elif row == '3' and column == '2':
		if board[17] == b:
			board.pop(17)
			board.insert(17, w)
			if board[22] == b:
				board.pop(22)
				board.insert(22, w)
				if board[12] == b:
					board.pop(12)
					board.insert(12, w)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
				else:
					board.pop(12)
					board.insert(12, b)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
			else:
				board.pop(22)
				board.insert(22, b)
				if board[12] == b:
					board.pop(12)
					board.insert(12, w)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
				else:
					board.pop(12)
					board.insert(12, b)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
		else:
			board.pop(17)
			board.insert(17, b)
			if board[22] == b:
				board.pop(22)
				board.insert(22, w)
				if board[12] == b:
					board.pop(12)
					board.insert(12, w)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
				else:
					board.pop(12)
					board.insert(12, b)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
			else:
				board.pop(22)
				board.insert(22, b)
				if board[12] == b:
					board.pop(12)
					board.insert(12, w)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
				else:
					board.pop(12)
					board.insert(12, b)
					if board[18] == b:
						board.pop(18)
						board.insert(18, w)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
					else:
						board.pop(18)
						board.insert(18, b)
						if board[16] == b:
							board.pop(16)
							board.insert(16, w)
							play5()
						else:
							board.pop(16)
							board.insert(16, b)
							play5()
	elif row == '3' and column == '3':
		if board[18] == b:
			board.pop(18)
			board.insert(18, w)
			if board[23] == b:
				board.pop(23)
				board.insert(23, w)
				if board[13] == b:
					board.pop(13)
					board.insert(13, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
				else:
					board.pop(13)
					board.insert(13, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
			else:
				board.pop(23)
				board.insert(23, b)
				if board[13] == b:
					board.pop(13)
					board.insert(13, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
				else:
					board.pop(13)
					board.insert(13, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
		else:
			board.pop(18)
			board.insert(18, b)
			if board[23] == b:
				board.pop(23)
				board.insert(23, w)
				if board[13] == b:
					board.pop(13)
					board.insert(13, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
				else:
					board.pop(13)
					board.insert(13, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
			else:
				board.pop(23)
				board.insert(23, b)
				if board[13] == b:
					board.pop(13)
					board.insert(13, w)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
				else:
					board.pop(13)
					board.insert(13, b)
					if board[19] == b:
						board.pop(19)
						board.insert(19, w)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
					else:
						board.pop(19)
						board.insert(19, b)
						if board[17] == b:
							board.pop(17)
							board.insert(17, w)
							play5()
						else:
							board.pop(17)
							board.insert(17, b)
							play5()
	elif row == '3' and column == '4':
		if board[19] == b:
			board.pop(19)
			board.insert(19, w)
			if board[18] == b:
				board.pop(18)
				board.insert(18, w)
				if board[14] == b:
					board.pop(14)
					board.insert(14, w)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
				else:
					board.pop(14)
					board.insert(14, b)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
			else:
				board.pop(18)
				board.insert(18, b)
				if board[14] == b:
					board.pop(14)
					board.insert(14, w)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
				else:
					board.pop(14)
					board.insert(14, b)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
		else:
			board.pop(19)
			board.insert(19, b)
			if board[18] == b:
				board.pop(18)
				board.insert(18, w)
				if board[14] == b:
					board.pop(14)
					board.insert(14, w)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
				else:
					board.pop(14)
					board.insert(14, b)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
			else:
				board.pop(18)
				board.insert(18, b)
				if board[14] == b:
					board.pop(14)
					board.insert(14, w)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
				else:
					board.pop(14)
					board.insert(14, b)
					if board[24] == b:
						board.pop(24)
						board.insert(24, w)
						play5()
					else:
						board.pop(24)
						board.insert(24, b)
						play5()
	elif row == '4' and column == '0':
		if board[20] == b:
			board.pop(20)
			board.insert(20, w)
			if board[15] == b:
				board.pop(15)
				board.insert(15, w)
				if board[21] == b:
					board.pop(21)
					board.insert(21, w)
					play5()
				else:
					board.pop(21)
					board.insert(21, b)
					play5()
			else:
				board.pop(15)
				board.insert(15, b)
				if board[21] == b:
					board.pop(21)
					board.insert(21, w)
					play5()
				else:
					board.pop(21)
					board.insert(21, b)
					play5()
		else:
			board.pop(20)
			board.insert(20, b)
			if board[15] == b:
				board.pop(15)
				board.insert(15, w)
				if board[21] == b:
					board.pop(21)
					board.insert(21, w)
					play5()
				else:
					board.pop(21)
					board.insert(21, b)
					play5()
			else:
				board.pop(15)
				board.insert(15, b)
				if board[21] == b:
					board.pop(21)
					board.insert(21, w)
					play5()
				else:
					board.pop(21)
					board.insert(21, b)
					play5()
	elif row == '4' and column == '1':
		if board[21] == b:
			board.pop(21)
			board.insert(21, w)
			if board[16] == b:
				board.pop(16)
				board.insert(16, w)
				if board[22] == b:
					board.pop(22)
					board.insert(22, w)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
				else:
					board.pop(22)
					board.insert(22, b)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
			else:
				board.pop(16)
				board.insert(16, b)
				if board[22] == b:
					board.pop(22)
					board.insert(22, w)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
				else:
					board.pop(22)
					board.insert(22, b)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
		else:
			board.pop(21)
			board.insert(21, b)
			if board[16] == b:
				board.pop(16)
				board.insert(16, w)
				if board[22] == b:
					board.pop(22)
					board.insert(22, w)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
				else:
					board.pop(22)
					board.insert(22, b)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
			else:
				board.pop(16)
				board.insert(16, b)
				if board[22] == b:
					board.pop(22)
					board.insert(22, w)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
				else:
					board.pop(22)
					board.insert(22, b)
					if board[20] == b:
						board.pop(20)
						board.insert(20, w)
						play5()
					else:
						board.pop(20)
						board.insert(20, b)
						play5()
	elif row == '4' and column == '2':
		if board[22] == b:
			board.pop(22)
			board.insert(22, w)
			if board[17] == b:
				board.pop(17)
				board.insert(17, w)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
				else:
					board.pop(23)
					board.insert(23, b)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
			else:
				board.pop(17)
				board.insert(17, b)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
				else:
					board.pop(23)
					board.insert(23, b)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
		else:
			board.pop(22)
			board.insert(22, b)
			if board[17] == b:
				board.pop(17)
				board.insert(17, w)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
				else:
					board.pop(23)
					board.insert(23, b)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
			else:
				board.pop(17)
				board.insert(17, b)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
				else:
					board.pop(23)
					board.insert(23, b)
					if board[21] == b:
						board.pop(21)
						board.insert(21, w)
						play5()
					else:
						board.pop(21)
						board.insert(21, b)
						play5()
	elif row == '4' and column == '3':
		if board[23] == b:
			board.pop(23)
			board.insert(23, w)
			if board[18] == b:
				board.pop(18)
				board.insert(18, w)
				if board[24] == b:
					board.pop(24)
					board.insert(24, w)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
				else:
					board.pop(24)
					board.insert(24, b)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
			else:
				board.pop(18)
				board.insert(18, b)
				if board[24] == b:
					board.pop(24)
					board.insert(24, w)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
				else:
					board.pop(24)
					board.insert(24, b)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
		else:
			board.pop(23)
			board.insert(23, b)
			if board[18] == b:
				board.pop(18)
				board.insert(18, w)
				if board[24] == b:
					board.pop(24)
					board.insert(24, w)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
				else:
					board.pop(24)
					board.insert(24, b)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
			else:
				board.pop(18)
				board.insert(18, b)
				if board[24] == b:
					board.pop(24)
					board.insert(24, w)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
				else:
					board.pop(24)
					board.insert(24, b)
					if board[22] == b:
						board.pop(22)
						board.insert(22, w)
						play5()
					else:
						board.pop(22)
						board.insert(22, b)
						play5()
	elif row == '4' and column == '4':
		if board[24] == b:
			board.pop(24)
			board.insert(24, w)
			if board[19] == b:
				board.pop(19)
				board.insert(19, w)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					play5()
				else:
					board.pop(23)
					board.insert(23, b)
					play5()
			else:
				board.pop(19)
				board.insert(19, b)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					play5()
				else:
					board.pop(23)
					board.insert(23, b)
					play5()
		else:
			board.pop(24)
			board.insert(24, b)
			if board[19] == b:
				board.pop(19)
				board.insert(19, w)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					play5()
				else:
					board.pop(23)
					board.insert(23, b)
					play5()
			else:
				board.pop(19)
				board.insert(19, b)
				if board[23] == b:
					board.pop(23)
					board.insert(23, w)
					play5()
				else:
					board.pop(23)
					board.insert(23, b)
					play5()
#needs to be last play	
def play5():
	if board != SolvedBoard:
		global PuzzleSolve
		PuzzleSolve = 0

def userint():
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
