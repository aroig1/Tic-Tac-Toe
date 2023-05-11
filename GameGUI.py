import tkinter as tk

class gameGUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("600x700")
        self.root.title("Tic-Tac-Toe")

        self.label = tk.Label(self.root, text="Tic-Tac-Toe", font=('Arial', 30))
        self.label.pack(pady=40)

        self.gameFrame = tk.Frame(self.root, background="Black", borderwidth=2)
        self.gameFrame.columnconfigure(0, weight=2)
        self.gameFrame.columnconfigure(1, weight=2)
        self.gameFrame.columnconfigure(2, weight=2)
        self.gameFrame.pack(padx=20, pady=50, fill='x')

        self.btn1 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

        self.btn7 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.btn8 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.gameFrame, text="", font=('Arial', 25))
        self.btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.root.mainloop()

gameGUI()