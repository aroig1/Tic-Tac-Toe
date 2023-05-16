import tkinter as tk

class gameGUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.gameBoard = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.turn = "X"
        self.turnCounter = 0
        self.gameRunning = True
        self.difficulty = "hard"
        self.difficultyChosen = False
        self.gameOpen = True

        # Window
        self.root.geometry("600x700")
        self.root.title("Tic-Tac-Toe")
        self.root.configure(background="light blue")

        # Game Title
        self.label = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 40), background="light blue")
        self.label.pack(pady=30)

        #Button Frame
        self.gameFrame = tk.Frame(self.root, background="Black", borderwidth=2)
        self.gameFrame.columnconfigure(0, weight=1)
        self.gameFrame.columnconfigure(1, weight=1)
        self.gameFrame.columnconfigure(2, weight=1)
        self.gameFrame.pack(padx=20, pady=30, fill='x')

        # Buttons
        self.btn = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for x in range(3):
            for y in range(3):
                self.btn[x][y] = tk.Button(self.gameFrame, text="", font=('Arial', 25), command=lambda x=x, y=y : self.takeTurn(x, y))
                self.btn[x][y].grid(row=x, column=y, sticky=tk.W+tk.E)

        # Turn Indicator
        self.turnLabel = tk.Label(self.root, text=("It is " + self.turn + " turn"), font=('Arial', 20), background="light blue")
        self.turnLabel.pack(pady=10)

        # Selection/Win Message
        self.message = tk.Label(self.root, text="", font=('Arial', 20), background="light blue")
        self.message.pack(pady=10)
        
        # Play Again Button
        self.playAgainBtn = tk.Button(self.root, text="Play Again", font=('Arial', 20), command=self.PlayAgain)
        self.playAgainBtn.pack_forget()

        #Exit Game Button
        self.exitBtn = tk.Button(self.root, text="Exit Game", font=('Arial', 20), command=self.ExitGame)
        self.exitBtn.pack_forget()

        # Selecting Difficulty Label + Buttons
        self.difficultyLabel = tk.Label(self.root, text="Choose your difficulty:", font=('Arial', 20), background="light blue")
        self.difficultyLabel.pack_forget()
        self.easyBtn = tk.Button(self.root, text="Easy Mode", font=('Arial', 20), command=self.EasyMode)
        self.easyBtn.pack_forget()
        self.hardBtn = tk.Button(self.root, text="Hard Mode", font=('Arial', 20), command=self.HardMode)
        self.hardBtn.pack_forget()

        self.root.protocol("WM_DELETE_WINDOW", self.ExitGame)

    
    def updateGUI(self):
        self.root.update()

    def takeTurn(self, row, col):
        if self.gameRunning:
            if self.gameBoard[row][col] == -1:
                self.btn[row][col]['text'] = self.turn
                self.gameBoard[row][col] = self.turn
                self.message.configure(text="")
                self.turnCounter += 1
            else:
                self.message.configure(text="The space you chose is already being used")

    def ShowPlayAgainButton(self):
        self.playAgainBtn.pack(pady=20)
        self.exitBtn.pack(pady=10)

    def PlayAgain(self):
        self.playAgainBtn.pack_forget()
        self.exitBtn.pack_forget()
        self.gameRunning = True
        self.turnCounter = 0
        for x in range(3):
            for y in range(3):
                self.gameBoard[x][y] = -1
                self.btn[x][y]['text'] = ""

    def ExitGame(self):
        self.root.destroy()
        self.gameOpen = False

    def PickDifficulty(self):
        self.gameFrame.pack_forget()
        self.turnLabel.pack_forget()
        self.message.pack_forget()
        self.difficultyLabel.pack(pady=20)
        self.easyBtn.pack(pady=20)
        self.hardBtn.pack(pady=20)

    def EasyMode(self):
        self.difficulty = "easy"
        self.difficultyChosen = True

    def HardMode(self):
        self.difficulty = "hard"
        self.difficultyChosen = True
    
    def ShowGame(self):
        self.difficultyLabel.pack_forget()
        self.easyBtn.pack_forget()
        self.hardBtn.pack_forget()
        self.gameFrame.pack(padx=20, pady=30, fill='x')
        self.turnLabel.pack(pady=10)
        self.message.pack(pady=10)