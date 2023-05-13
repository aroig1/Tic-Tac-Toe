import tkinter as tk

class gameGUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.gameBoard = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.turn = "X"
        self.turnCounter = 0

        # Window
        self.root.geometry("600x700")
        self.root.title("Tic-Tac-Toe")
        self.root.configure(background="light blue")

        # Game Title
        self.label = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 30), background="light blue")
        self.label.pack(pady=40)

        #Button Frame
        self.gameFrame = tk.Frame(self.root, background="Black", borderwidth=2)
        self.gameFrame.columnconfigure(0, weight=1)
        self.gameFrame.columnconfigure(1, weight=1)
        self.gameFrame.columnconfigure(2, weight=1)
        self.gameFrame.pack(padx=20, pady=50, fill='x')

        # Buttons
        self.btn = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for x in range(3):
            for y in range(3):
                self.btn[x][y] = tk.Button(self.gameFrame, text="", font=('Arial', 25), command=lambda x=x, y=y : self.takeTurn(x, y))
                self.btn[x][y].grid(row=x, column=y, sticky=tk.W+tk.E)

        # Turn Indicator
        self.turnLabel = tk.Label(self.root, text=("It is " + self.turn + " turn"), font=('Arial', 20), background="light blue")
        self.turnLabel.pack(pady=20)

        # Selection/Win Message
        self.message = tk.Label(self.root, text="", font=('Arial', 20), background="light blue")
        self.message.pack(pady=20)

        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        #self.root.mainloop()
        #self.root.update()

    
    def updateGUI(self):
        self.root.update()
        pass

    def takeTurn(self, row, col):
        if self.gameBoard[row][col] == -1:
            self.btn[row][col]['text'] = self.turn
            self.gameBoard[row][col] = self.turn
            self.message.configure(text="")
            self.turnCounter += 1
        else:
            self.message.configure(text="The space you chose is already being used")
