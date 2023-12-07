import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ']*3 for _ in range(3)]
        self.create_board_buttons()

    def create_board_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('normal', 20), width=8, height=4,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button(row, col)
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Joueur {self.current_player} gagne !")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "Match nul !")
                self.reset_game()
            else:
                self.toggle_player()

    def update_button(self, row, col):
        button = self.root.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        lines = [
            self.board[row],                     # Check row
            [self.board[i][col] for i in range(3)],  # Check column
            [self.board[i][i] for i in range(3)],   # Check diagonal
            [self.board[i][2-i] for i in range(3)]  # Check anti-diagonal
        ]
        return any(all(cell == self.current_player for cell in line) for line in lines)

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[' ']*3 for _ in range(3)]
        for button in self.root.grid_slaves():
            button.config(text='', state=tk.NORMAL)
        self.current_player = 'X'

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
