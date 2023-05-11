import tkinter as tk

class gameGUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("600x700")
        self.root.title("Tic-Tac-Toe")

        self.label = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 30))
        self.label.pack(pady=40)

        self.gameFrame = tk.Frame(self.root, background="Black", borderwidth=2)
        self.gameFrame.columnconfigure(0, weight=1)
        self.gameFrame.columnconfigure(1, weight=1)
        self.gameFrame.columnconfigure(2, weight=1)
        self.gameFrame.pack(padx=20, pady=50, fill='x')

        self.btn = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for x in range(3):
            for y in range(3):
                self.btn[x][y] = tk.Button(self.gameFrame, text="", font=('Arial', 25))
                self.btn[x][y].grid(row=x, column=y, sticky=tk.W+tk.E)

        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        turnLabel = tk.Label(self.root, text="It is ___ turn", font=('Arial', 20))
        turnLabel.pack(pady=20)

        errorMessage = tk.Label(self.root, text="Insert turn error here", font=('Arial', 20))
        errorMessage.pack(pady=20)

        self.root.mainloop()

gameGUI()