# -*- coding: utf-8 -*-
"""
Tommy Le
CPSC 223P-01
Thu Feb 18 13:14:07 2021
tommyle@fullerton.edu
"""

import string
import random

computerWin = 0
userWin = 0
tieNumber = 0

while True:
  userinput = input("Make your choice: (R, P, S, Q) >\n")

  choices = ['r','p','s']
  computerinput = random.choice(choices)

  
  if (userinput.lower() == 'q'):
    break

  if userinput.lower() == computerinput:
    if computerinput == 'r':
      print("Computer chose Rock. Call it a draw.")
      tieNumber = tieNumber + 1
    elif(computerinput == 'p'):
      print("Computer chose Paper. Call it a draw.")
      tieNumber = tieNumber + 1
    else:
      print("Computer chose Scissors. Call it a draw")
      tieNumber = tieNumber + 1
  elif userinput.lower() == 'r':
    if computerinput == "s":
      print("Computer chose Scissors. You win.")
      userWin = userWin + 1
    else:
      print("Computer chose Paper. Computer wins.")
      computerWin = computerWin + 1
  elif userinput.lower() == 'p':
    if computerinput == 'r':
      print("Computer chose Rock. You win.")
      userWin = userWin + 1
    else:
      print("Computer chose Scissors. Computer wins.")
      computerWin = computerWin + 1
  elif userinput.lower() == 's':
    if computerinput == 'p':
      print("Computer chose Paper. You win.")
      userWin = userWin + 1
    else:
      print("Computer chose Rock. Computer wins.")
      computerWin = computerWin + 1
  else:
    print("Invalid entry. Try again")

if userinput.lower() == 'q':
  print("Computer:", computerWin)
  print("You: ", userWin)
  print("Ties: ", tieNumber)
  if(computerWin == userWin):
    print("You tied!")
  elif(computerWin > userWin):
    print("Computer won!")
  else:
    print("You won!")
