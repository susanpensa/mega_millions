"""
Program: megamillions.py
Author: Susan 11/19/21

***NOTE: the file breezypythongui.py must be in the same directory as this file for the application to work.***
***NOTE: file: logo.png must be in the same directory for the application to display properly.***
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage
import random

class MegaMillions(EasyFrame):
	
	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, title = "NY Lottery Mega Millions", width = 475, height = 400, background = "DodgerBlue", resizable = False)
		# Title label and image logo
		self.imageLabel = self.addLabel(text = "", row = 0, column = 0, background = "DodgerBlue", foreground = "red", sticky = "NSEW")
		self.image = PhotoImage(file = "logo.png")
		self.imageLabel["image"] = self.image
		self.addLabel(text = "Mega Millions", row  = 0, column = 1, columnspan = 5, background = "DodgerBlue", foreground = "red", font = Font(family = "Impact", size = 38), sticky = "NSEW")

		# Fields for the random lotto numbers to appear
		self.ball1 = self.addIntegerField(value = 0, row = 1, column = 0, sticky = "NSEW", state = "readonly")
		self.ball2 = self.addIntegerField(value = 0, row = 1, column = 1, sticky = "NSEW", state = "readonly")
		self.ball3 = self.addIntegerField(value = 0, row = 1, column = 2, sticky = "NSEW", state = "readonly")
		self.ball4 = self.addIntegerField(value = 0, row = 1, column = 3, sticky = "NSEW", state = "readonly")
		self.ball5 = self.addIntegerField(value = 0, row = 1, column = 4, sticky = "NSEW", state = "readonly")

		# Label and field for the Mega Ball number to appear
		self.addLabel(text = "Mega Ball", row = 2, column = 0, columnspan = 5, background = "DodgerBlue", foreground = "yellow", sticky = "NSEW", font = Font(family = "Impact", size = 36))
		self.megaBall = self.addIntegerField(value = 0, row = 3, column = 1, columnspan = 2, sticky = "NSEW", state = "readonly")
		
		# Command button to draw lotto numbers
		self.drawButton = self.addButton(text = "DRAW", row = 4, column = 0, columnspan = 5, command = self.play)

		# Label for the winning numbers
		self.outputLabel = self.addLabel(text = "Today's Winning Numbers", row = 5, column = 0, columnspan = 5, sticky = "NSEW", background = "DodgerBlue", foreground = "white", font = Font(family = "Impact", size = 18))

		# Fields for the winning numbers. Value changed daily by programmer
		self.win1 = self.addIntegerField(value = 4, row = 6, column = 0, sticky = "NSEW", state = "readonly")
		self.win2 = self.addIntegerField(value = 56, row = 6, column = 1, sticky = "NSEW", state = "readonly")
		self.win3 = self.addIntegerField(value = 11, row = 6, column = 2, sticky = "NSEW", state = "readonly")
		self.win4 = self.addIntegerField(value = 29, row = 6, column = 3, sticky = "NSEW", state = "readonly")
		self.win5 = self.addIntegerField(value = 37, row = 6, column = 4, sticky = "NSEW", state = "readonly")

	# Definition of play button
	def play(self):
		"""Draws and places users lotto ball and mega ball random numbers into IntegerField."""
		num1 = random.randint(1, 70)
		num2 = random.randint(1, 70)
		num3 = random.randint(1, 70)
		num4 = random.randint(1, 70)
		num5 = random.randint(1, 70)
		mega = random.randint(1, 25)

		# Output Phase
		self.ball1.setNumber(num1)
		self.ball2.setNumber(num2)
		self.ball3.setNumber(num3)
		self.ball4.setNumber(num4)
		self.ball5.setNumber(num5)
		self.megaBall.setNumber(mega)

# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	MegaMillions().mainloop()

# global call to the main() function
if __name__ == "__main__":
	main()