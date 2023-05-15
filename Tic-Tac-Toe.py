import random
from GameGUI import gameGUI

class TicTacToe:
    def __init__ (self):

        self.GUI = gameGUI()

        self.difficulty = "easy"
        self.turnCounter = 0
        self.keepPlaying = "yes"

    def checkForWin(self):
        for x in range(3):
            # Check for Horizontal
            if self.GUI.gameBoard[x][0] == self.GUI.gameBoard[x][1] == self.GUI.gameBoard[x][2] and self.GUI.gameBoard[x][0] != -1:
                print("HORIZONTAL", self.GUI.turn)
                return True
            
            # Check for Vertical
            elif self.GUI.gameBoard[0][x] == self.GUI.gameBoard[1][x] == self.GUI.gameBoard[2][x] and self.GUI.gameBoard[0][x] != -1:
                    print("VERTICAL", self.GUI.turn)
                    return True
        
        # Check for Diagonal
        if self.GUI.gameBoard[0][0] == self.GUI.gameBoard[1][1] == self.GUI.gameBoard[2][2] and self.GUI.gameBoard[0][0] != -1:
            print("DIAGONAL")
            return True
        elif self.GUI.gameBoard[0][2] == self.GUI.gameBoard[1][1] == self.GUI.gameBoard[2][0] and self.GUI.gameBoard[0][2] != -1:
            print("DIAGONAL 2")
            return True
        
        # No Win
        else:
            return False

    def checkForTie(self): ## NO IDEA HOW THIS WORKS
        if -1 in self.GUI.gameBoard: 
            print(self.GUI.gameBoard)
            return True
        else:
            return False

    def computerInput(self):
        print("Computer thinking...") ## DELETE

        # Easy Difficulty AI
        if self.difficulty == "easy":
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            while self.GUI.gameBoard[x][y] != -1:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
        """
        # Hard Difficulty AI
        if difficulty == "hard":
            options = [1]  ## DELETE
            #middle spot
            if 5 in options:
                selection = 5
            #corner spots for 1st turn
            elif 1 in options and turnCounter <= 2:
                selection = 1
            elif 3 in options and turnCounter <= 2:
                selection = 3
            elif 7 in options and turnCounter <= 2:
                selection = 7
            elif 9 in options and turnCounter <= 2:
                selection = 9
            #potential winning moves(top row)(left to right)
            elif 1 in options and ((gameBoard[1] == "O" and gameBoard[2] == "O") or (gameBoard[3] == "O" and gameBoard[6] == "O") or (gameBoard[4] == "O" and gameBoard[8] == "O")):
                selection = 1
            elif 2 in options and ((gameBoard[0] == "O" and gameBoard[2] == "O") or (gameBoard[4] == "O" and gameBoard[7] == "O")):
                selection = 2
            elif 3 in options and ((gameBoard[0] == "O" and gameBoard[1] == "O") or (gameBoard[5] == "O" and gameBoard[8] == "O") or (gameBoard[4] == "O" and gameBoard[6] == "O")):
                selection = 3
            #potential winning moves(middle row)(left and right)
            elif 4 in options and ((gameBoard[4] == "O" and gameBoard[5] == "O") or (gameBoard[0] == "O" and gameBoard[6] == "O")):
                selection = 4
            elif 6 in options and ((gameBoard[3] == "O" and gameBoard[4] == "O") or (gameBoard[2] == "O" and gameBoard[8] == "O")):
                selection = 6
            #potential winning moves(bottom row)(left to right)
            elif 7 in options and ((gameBoard[7] == "O" and gameBoard[8] == "O") or (gameBoard[0] == "O" and gameBoard[3] == "O") or (gameBoard[4] == "O" and gameBoard[2] == "O")):
                selection = 7
            elif 8 in options and ((gameBoard[6] == "O" and gameBoard[8] == "O") or (gameBoard[4] == "O" and gameBoard[1] == "O")):
                selection = 8
            elif 9 in options and ((gameBoard[6] == "O" and gameBoard[7] == "O") or (gameBoard[2] == "O" and gameBoard[5] == "O") or (gameBoard[4] == "O" and gameBoard[0] == "O")):
                selection = 9
            #corner blocks
            elif 1 in options and ((gameBoard[1] == "X" and gameBoard[2] == "X") or (gameBoard[3] == "X" and gameBoard[6] == "X") or (gameBoard[4] == "X" and gameBoard[8] == "X")):
                selection = 1
            elif 3 in options and ((gameBoard[0] == "X" and gameBoard[1] == "X") or (gameBoard[5] == "X" and gameBoard[8] == "X") or (gameBoard[4] == "X" and gameBoard[6] == "X")):
                selection = 3
            elif 7 in options and ((gameBoard[0] == "X" and gameBoard[3] == "X") or (gameBoard[7] == "X" and gameBoard[8] == "X") or (gameBoard[4] == "X" and gameBoard[2] == "X")):
                selection = 7
            elif 9 in options and ((gameBoard[2] == "X" and gameBoard[5] == "X") or (gameBoard[6] == "X" and gameBoard[7] == "X") or (gameBoard[4] == "X" and gameBoard[0] == "X")):
                selection = 9
            #middle edge spots for 2nd turn when AI has middle spot
            elif 2 in options and gameBoard[4] == "O" and (gameBoard[0] == "X" and gameBoard[2] == "X"):
                selection = 2
            elif 4 in options and gameBoard[4] == "O" and (gameBoard[0] == "X" and gameBoard[6] == "X"):
                selection = 4
            elif 6 in options and gameBoard[4] == "O" and (gameBoard[2] == "X" and gameBoard[8] == "X"):
                selection = 6
            elif 8 in options and gameBoard[4] == "O" and (gameBoard[6] == "X" and gameBoard[8] == "X"):
                selection = 8
            elif 2 in options and gameBoard[4] == "O" and gameBoard[0] == "X" and gameBoard[8] == "X":
                selection = 2
            elif 2 in options and gameBoard[4] == "O" and gameBoard[2] == "X" and gameBoard[6] == "X":
                selection = 2
            #middle edge spots for 2nd turn when AI has corner spot
            elif 2 in options and (gameBoard[0] == "O" or gameBoard[2] == "O") and (gameBoard[0] != "X" and gameBoard[2] != "X"):
                selection = 2
            elif 4 in options and (gameBoard[0] == "O" or gameBoard[6] == "O") and (gameBoard[0] != "X" and gameBoard[6] != "X"):
                selection = 4
            elif 6 in options and (gameBoard[2] == "O" or gameBoard[8] == "O") and (gameBoard[2] != "X" and gameBoard[8] != "X"):
                selection = 6
            elif 8 in options and (gameBoard[6] == "O" or gameBoard[8] == "O") and (gameBoard[6] != "X" and gameBoard[8] != "X"):
                selection = 8
            #RANDOM (temporary) (MODIFY??)
            else:
                selection = random.randint(1, 9)
                while selection not in options:
                    selection = random.randint(1, 9) """
        
        self.GUI.takeTurn(x, y)
            

    def runGame(self):

        #self.difficulty = input("Choose your difficulty? (easy, hard): ")
        while (self.keepPlaying == "yes"):
            self.GUI.gameRunning = True

            while self.GUI.gameRunning:
                self.GUI.updateGUI()
                print(self.GUI.turnCounter, self.GUI.turn) ## DELETE
                if self.checkForWin() and self.GUI.turn == "X":
                    self.GUI.message.configure(text="YOU WON!!!")
                    print("YOU WON!!!")
                    self.GUI.gameRunning = False
                elif self.checkForWin() and self.GUI.turn == "O":
                    print(self.GUI.gameBoard)
                    self.GUI.message.configure(text="YOU SUCK!!!")
                    print("YOU SUCK.")
                    self.GUI.gameRunning = False
                elif self.checkForTie():
                    self.GUI.message.configure(text="YOU TIED!!!")
                    print("YOU TIED")
                    self.GUI.gameRunning = False
                elif self.GUI.turnCounter % 2 == 0:
                    self.GUI.turn = "X"
                else:
                    self.GUI.turn = "O"
                    self.computerInput()
            
            self.GUI.updateGUI()
            self.keepPlaying = input("\nDo you want to play again? (yes/no): ")
        print("\nGoodbye\n")

if __name__ == '__main__':
    game = TicTacToe()
    game.runGame()