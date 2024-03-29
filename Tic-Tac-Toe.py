import random
import os
import openai
from GameGUI import gameGUI

class TicTacToe:
    def __init__ (self):

        self.GUI = gameGUI()

    def checkForWin(self):
        for x in range(3):
            # Check for Horizontal
            if self.GUI.gameBoard[x][0] == self.GUI.gameBoard[x][1] == self.GUI.gameBoard[x][2] and self.GUI.gameBoard[x][0] != -1:
                return True
            
            # Check for Vertical
            elif self.GUI.gameBoard[0][x] == self.GUI.gameBoard[1][x] == self.GUI.gameBoard[2][x] and self.GUI.gameBoard[0][x] != -1:
                    return True
        
        # Check for Diagonal
        if self.GUI.gameBoard[0][0] == self.GUI.gameBoard[1][1] == self.GUI.gameBoard[2][2] and self.GUI.gameBoard[0][0] != -1:
            return True
        elif self.GUI.gameBoard[0][2] == self.GUI.gameBoard[1][1] == self.GUI.gameBoard[2][0] and self.GUI.gameBoard[0][2] != -1:
            return True
        
        # No Win
        else:
            return False

    def checkForTie(self):
        if self.GUI.turnCounter >= 9:
            return True
        else:
            return False

    def computerInput(self):

        # Easy Difficulty AI
        if self.GUI.difficulty == "easy":
            selX = random.randint(0, 2)
            selY = random.randint(0, 2)
            while self.GUI.gameBoard[selX][selY] != -1:
                selX = random.randint(0, 2)
                selY = random.randint(0, 2)
        
        # Hard Difficulty AI
        if self.GUI.difficulty == "hard":
            #middle spot
            if self.GUI.gameBoard[1][1] == -1:
                selX = 1
                selY = 1
            #corner spots for 1st turn
            elif self.GUI.gameBoard[0][0] == -1 and self.GUI.turnCounter <= 2:
                selX = 0
                selY = 0
            elif self.GUI.gameBoard[0][2] == -1 and self.GUI.turnCounter <= 2:
                selX = 0
                selY = 2
            elif self.GUI.gameBoard[2][0] == -1 and self.GUI.turnCounter <= 2:
                selX = 2
                selY = 0
            elif self.GUI.gameBoard[2][2] == -1 and self.GUI.turnCounter <= 2:
                selX = 2
                selY = 2
            #potential winning moves(top row)(left to right)
            elif self.GUI.gameBoard[0][0] == -1 and ((self.GUI.gameBoard[0][1] == "O" and self.GUI.gameBoard[0][2] == "O") or (self.GUI.gameBoard[1][0] == "O" and self.GUI.gameBoard[2][0] == "O") or (self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[2][2] == "O")):
                selX = 0
                selY = 0
            elif self.GUI.gameBoard[0][1] == -1 and ((self.GUI.gameBoard[0][0] == "O" and self.GUI.gameBoard[0][2] == "O") or (self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[2][1] == "O")):
                selX = 0
                selY = 1
            elif self.GUI.gameBoard[0][2] == -1 and ((self.GUI.gameBoard[0][0] == "O" and self.GUI.gameBoard[0][1] == "O") or (self.GUI.gameBoard[1][2] == "O" and self.GUI.gameBoard[2][2] == "O") or (self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[2][0] == "O")):
                selX = 0
                selY = 2
            #potential winning moves(middle row)(left and right)
            elif self.GUI.gameBoard[1][0] == -1 and ((self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[1][2] == "O") or (self.GUI.gameBoard[0][0] == "O" and self.GUI.gameBoard[2][0] == "O")):
                selX = 1
                selY = 0
            elif self.GUI.gameBoard[1][2] == -1 and ((self.GUI.gameBoard[1][0] == "O" and self.GUI.gameBoard[1][1] == "O") or (self.GUI.gameBoard[0][2] == "O" and self.GUI.gameBoard[2][2] == "O")):
                selX = 1
                selY = 2
            #potential winning moves(bottom row)(left to right)
            elif self.GUI.gameBoard[2][0] == -1 and ((self.GUI.gameBoard[2][1] == "O" and self.GUI.gameBoard[2][2] == "O") or (self.GUI.gameBoard[0][0] == "O" and self.GUI.gameBoard[1][0] == "O") or (self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[0][2] == "O")):
                selX = 2
                selY = 0
            elif self.GUI.gameBoard[2][1] == -1 and ((self.GUI.gameBoard[2][0] == "O" and self.GUI.gameBoard[2][2] == "O") or (self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[0][1] == "O")):
                selX = 2
                selY = 1
            elif self.GUI.gameBoard[2][2] == -1 and ((self.GUI.gameBoard[2][0] == "O" and self.GUI.gameBoard[2][1] == "O") or (self.GUI.gameBoard[0][2] == "O" and self.GUI.gameBoard[1][2] == "O") or (self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[0][0] == "O")):
                selX = 2
                selY = 2
            #corner blocks
            elif self.GUI.gameBoard[0][0] == -1 and ((self.GUI.gameBoard[0][1] == "X" and self.GUI.gameBoard[0][2] == "X") or (self.GUI.gameBoard[1][0] == "X" and self.GUI.gameBoard[2][0] == "X") or (self.GUI.gameBoard[1][1] == "X" and self.GUI.gameBoard[2][2] == "X")):
                selX = 0
                selY = 0
            elif self.GUI.gameBoard[0][2] == -1 and ((self.GUI.gameBoard[0][0] == "X" and self.GUI.gameBoard[0][1] == "X") or (self.GUI.gameBoard[1][2] == "X" and self.GUI.gameBoard[2][2] == "X") or (self.GUI.gameBoard[1][1] == "X" and self.GUI.gameBoard[2][0] == "X")):
                selX = 0
                selY = 2
            elif self.GUI.gameBoard[2][0] == -1 and ((self.GUI.gameBoard[0][0] == "X" and self.GUI.gameBoard[1][0] == "X") or (self.GUI.gameBoard[2][1] == "X" and self.GUI.gameBoard[2][2] == "X") or (self.GUI.gameBoard[1][1] == "X" and self.GUI.gameBoard[0][2] == "X")):
                selX = 2
                selY = 0
            elif self.GUI.gameBoard[2][2]  == -1 and ((self.GUI.gameBoard[0][2] == "X" and self.GUI.gameBoard[1][2] == "X") or (self.GUI.gameBoard[2][0] == "X" and self.GUI.gameBoard[2][1] == "X") or (self.GUI.gameBoard[1][1] == "X" and self.GUI.gameBoard[0][0] == "X")):
                selX = 2
                selY = 2
            #middle edge blocks
            elif self.GUI.gameBoard[2][1] == -1 and self.GUI.gameBoard[0][1] == self.GUI.gameBoard[1][1] == "X":
                selX = 2
                selY = 1
            elif self.GUI.gameBoard[1][0] == -1 and self.GUI.gameBoard[1][2] == self.GUI.gameBoard[1][1] == "X":
                selX = 1
                selY = 0
            elif self.GUI.gameBoard[0][1] == -1 and self.GUI.gameBoard[2][1] == self.GUI.gameBoard[1][1] == "X":
                selX = 0
                selY = 1
            elif self.GUI.gameBoard[1][2] == -1 and self.GUI.gameBoard[1][0] == self.GUI.gameBoard[1][1] == "X":
                selX = 1
                selY = 2

            #middle edge spots for 2nd turn when AI has middle spot
            elif self.GUI.gameBoard[0][1]  == -1 and self.GUI.gameBoard[1][1] == "O" and (self.GUI.gameBoard[0][0] == "X" and self.GUI.gameBoard[0][2] == "X"):
                selX = 0
                selY = 1
            elif self.GUI.gameBoard[1][0] == -1 and self.GUI.gameBoard[1][1] == "O" and (self.GUI.gameBoard[0][0] == "X" and self.GUI.gameBoard[2][0] == "X"):
                selX = 1
                selY = 0
            elif self.GUI.gameBoard[1][2] == -1 and self.GUI.gameBoard[1][1] == "O" and (self.GUI.gameBoard[0][2] == "X" and self.GUI.gameBoard[2][2] == "X"):
                selX = 1
                selY = 2
            elif self.GUI.gameBoard[2][1] == -1 and self.GUI.gameBoard[1][1] == "O" and (self.GUI.gameBoard[2][0] == "X" and self.GUI.gameBoard[2][2] == "X"):
                selX = 2
                selY = 1
            elif self.GUI.gameBoard[0][1] == -1 and self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[0][0] == "X" and self.GUI.gameBoard[2][2] == "X":
                selX = 0
                selY = 1
            elif self.GUI.gameBoard[0][1] == -1 and self.GUI.gameBoard[1][1] == "O" and self.GUI.gameBoard[0][2] == "X" and self.GUI.gameBoard[2][0] == "X":
                selX = 0
                selY = 1
                
            #middle edge spots for 2nd turn when AI has corner spot
            elif self.GUI.gameBoard[0][1] == -1 and (self.GUI.gameBoard[0][0] == "O" or self.GUI.gameBoard[0][2] == "O") and (self.GUI.gameBoard[0][0] != "X" and self.GUI.gameBoard[0][2] != "X"):
                selX = 0
                selY = 1
            elif self.GUI.gameBoard[1][0] == -1 and (self.GUI.gameBoard[0][0] == "O" or self.GUI.gameBoard[2][0] == "O") and (self.GUI.gameBoard[0][0] != "X" and self.GUI.gameBoard[2][0] != "X"):
                selX = 1
                selY = 0
            elif self.GUI.gameBoard[1][2] == -1 and (self.GUI.gameBoard[0][2] == "O" or self.GUI.gameBoard[2][2] == "O") and (self.GUI.gameBoard[0][2] != "X" and self.GUI.gameBoard[2][2] != "X"):
                selX = 1
                selY = 2
            elif self.GUI.gameBoard[2][1] == -1 and (self.GUI.gameBoard[2][0] == "O" or self.GUI.gameBoard[2][2] == "O") and (self.GUI.gameBoard[2][0] != "X" and self.GUI.gameBoard[2][2] != "X"):
                selX = 2
                selY = 1
            #RANDOM (temporary) (MODIFY??)
            else:
                selX = random.randint(0, 2)
                selY = random.randint(0, 2)
                while self.GUI.gameBoard[selX][selY] != -1:
                    selX = random.randint(0, 2)
                    selY = random.randint(0, 2)
        
        # ChatGPT AI Difficulty
        if self.GUI.difficulty == "ai":
            openai.api_key = "API_KEY"

            # Call to ChatGPT API for response, inputting gameBoard
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are my tic tac toe opponent."},
                {"role": "user", "content": f"This is a tic tac toe game board {self.GUI.gameBoard}. Reply with only the coordinates of your turn in the 2D list, no other text. Ex: [0,0] would be the top left corner. You are O's and I am X's. -1 represents an empty space."}
            ],
            temperature=0.8
            )

            turn = completion.choices[0].message.content

            # Remove spaces or any words from ChatGPT's response
            turn = ''.join(c for c in turn if not c.isalpha())
            turn = ''.join(c for c in turn if not c == ' ')

            selX = int(turn[1])
            selY = int(turn[3])
            
        self.GUI.takeTurn(selX, selY)

    def runGame(self):
        self.GUI.PickDifficulty()
        self.GUI.updateGUI()
        
        while (self.GUI.gameOpen):
            if self.GUI.difficultyChosen:
                break
            self.GUI.updateGUI()

        if self.GUI.gameOpen:
            self.GUI.ShowGame()

        while (self.GUI.gameOpen):
            
            while self.GUI.gameRunning and self.GUI.gameOpen:
                self.GUI.updateGUI()
                if self.checkForWin() and self.GUI.turn == "X":
                    self.GUI.message.configure(text="YOU WON!!!")
                    self.GUI.wins += 1
                    self.GUI.gameRunning = False
                elif self.checkForWin() and self.GUI.turn == "O":
                    self.GUI.message.configure(text="YOU SUCK!!!")
                    self.GUI.losses += 1
                    self.GUI.gameRunning = False
                elif self.checkForTie():
                    self.GUI.message.configure(text="YOU TIED!!!")
                    self.GUI.ties += 1
                    self.GUI.gameRunning = False
                elif self.GUI.turnCounter % 2 == 0:
                    self.GUI.turn = "X"
                else:
                    self.GUI.turn = "O"
                    self.computerInput()
            
            if self.GUI.gameOpen:
                self.GUI.ShowPlayAgainButton()
                self.GUI.updateGUI()
           
if __name__ == '__main__':
    game = TicTacToe()
    game.runGame()