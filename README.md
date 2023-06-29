**This is a lab from my Python Class**

# Background
Rock, Paper, Scissors is a popular game often played by children, or child-like adults. It is sometimes used as a method of selection similar to flipping a coin or throwing dice to randomly select a person for some purpose.  Of course, this game is not truly random since a skilled player can often recognize and exploit the non-random behavior of an opponent.  For instance, if you notice that your opponent chooses Paper most frequently, you may choose Scissors (which beats Paper) most often in an effort to win. There are many variants of this game.

# Rules of the Game:
The objective of Rock, Paper, Scissors is to defeat your opponent by selecting a weapon that defeats their choice under the following rules:
- Rock smashes Scissors (so Rock wins)
- Scissors cuts Paper (so Scissors win)
- Paper covers Rock (so Paper wins)
- If the players choose the same weapon, neither win and the game is played again

# Requirements
1. Your program shall first choose a computer weapon to play against the user, but not display the weapon until after the user has selected.
2. Your program shall then announce the beginning of the round and use the function input() to prompt the user for their weapon of choice.
3. Your program shall compare the two weapons and determine a winner (or a tie) and the results shall be displayed using print().
    
    For example, if the user chooses 'r' for Rock, the format of the three possible outcomes shall be as follows:
  > Computer chose Rock. Call it a draw.  
  > Computer chose Paper. Computer wins!  
  > Computer chose Scissors. You win!
4. Your program shall continue looping for user input until the user types "q" to end the game.
5. Your program shall handle an inivalid user entry by letting the user know their selection was invalid. (Use the word "Invalid" in your feedback)
5. Your program shall keep track of wins, losses and ties and display the final "score board" at the end of the game.

    Here are three examples of the end-of-game score board format:
    > Computer: 4  
    You: 4  
    Ties: 3  
    You tied!

    > Computer: 5  
    You: 3  
    Ties: 3  
    Computer won!

    > Computer: 5  
    You: 7  
    Ties: 3  
    You won!


# Specifications
At the beginning of each round your program should ask the user for input.  To make it easier on the user, they are only required to enter a single letter, R, P, S or Q.  Be prepared to handle upper or lower case entries.  If the user inputs something other than the legal entries, you will have to handle that too.  But for the sake of output, you will need to print the full word (Rock, Paper, or Scissors).  The user should be able to play as many times as he/she wants, then after typing 'q' for quit, the program will display the final score as shown above.  See _example_output.txt_ for a sample of what a full game's worth of output should look like.
