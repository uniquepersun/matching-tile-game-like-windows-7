import tkinter as tk
from tkinter import messagebox
import random
import time

class tilegame:
    def __init__(self, root):
        self.root = root
        self.root.title("tile matching game")
        self.icons = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'] * 2
        random.shuffle(self.icons)
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        self.flipped = [[False for _ in range(4)] for _ in range(4)]
        self.first = None
        self.second = None
        self.create_widgets()
        self.update_buttons()

    def create_widgets(self):
        for i in range(4):
            for j in range(4):
                button = tk.Button(self.root, text='', width=6, height=3, command=lambda r=i, c=j: self.on_button_click(r, c))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.reset_button = tk.Button(self.root, text="New Game", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=4)

    def update_buttons(self):
        for i in range(4):
            for j in range(4):
                if self.flipped[i][j]:
                    self.buttons[i][j].config(text=self.icons[i * 4 + j], state=tk.DISABLED)
                else:
                    self.buttons[i][j].config(text='', state=tk.NORMAL)

    def on_button_click(self, row, col):
        if self.flipped[row][col] or (self.first and self.second):
            return
    
        self.buttons[row][col].config(text=self.icons[row * 4 + col])
        self.flipped[row][col] = True
        
        if not self.first:
            self.first = (row, col)
        elif not self.second:
            self.second = (row, col)
            self.root.after(1000, self.check_match)
    
    def check_match(self):
        r1, c1 = self.first
        r2, c2 = self.second

        if self.icons[r1 * 4 + c1] != self.icons[r2 * 4 + c2]:
            self.flipped[r1][c1] = self.flipped[r2][c2] = False
            self.update_buttons()
        
        self.first = self.second = None
        
        if all(all(row) for row in self.flipped):
            messagebox.showinfo("congrats!", "you won!!")

    def reset_game(self):
        self.icons = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'] * 2
        random.shuffle(self.icons)
        self.flipped = [[False for _ in range(4)] for _ in range(4)]
        self.first = self.second = None
        self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    game = tilegame(root)
    root.mainloop()
