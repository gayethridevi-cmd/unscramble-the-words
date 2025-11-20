import random
import tkinter as tk
from tkinter import messagebox

# Function for choosing a random word
def choose():
    words = ["SEPARATE", "DEFINITELY", "OCCURRENCE", "CONSENSUS", "ACCEPTABLE",
             "BROCCOLI", "REFERRED", "BUREAUCRACY", "BISHOP", "PROGRAMMING",
             "ENTREPRENEUR", "CONSCIENCE", "PARALLEL", "CENTRE"]
    return random.choice(words)

# Function to jumble characters of the chosen word
def jumble(word):
    return ''.join(random.sample(word, len(word)))

class WordGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Jumble Game")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff")

        # Player names
        self.p1name = tk.StringVar()
        self.p2name = tk.StringVar()

        # Scores
        self.p1score = 0
        self.p2score = 0
        self.turn = 0

        # Game word
        self.picked_word = ""
        self.jumbled_word = ""

        # UI setup
        self.setup_start_screen()

    def setup_start_screen(self):
        tk.Label(self.root, text="Enter Player 1 Name:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.p1name).pack(pady=5)

        tk.Label(self.root, text="Enter Player 2 Name:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.p2name).pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.start_game, bg="green", fg="white").pack(pady=20)

    def start_game(self):
        self.clear_screen()
        self.next_round()

    def next_round(self):
        self.picked_word = choose()
        self.jumbled_word = jumble(self.picked_word)

        tk.Label(self.root, text=f"Jumbled word: {self.jumbled_word}", font=("Arial", 16), bg="#f0f8ff").pack(pady=20)

        current_player = self.p1name.get() if self.turn % 2 == 0 else self.p2name.get()
        tk.Label(self.root, text=f"{current_player}, it's your turn!", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)

        self.answer_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.answer_var, font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Submit", command=self.check_answer, bg="blue", fg="white").pack(pady=10)

    def check_answer(self):
        answer = self.answer_var.get().strip().upper()
        current_player = self.p1name.get() if self.turn % 2 == 0 else self.p2name.get()

        if answer == self.picked_word:
            if self.turn % 2 == 0:
                self.p1score += 1
            else:
                self.p2score += 1
            messagebox.showinfo("Correct!", f"Well done {current_player}! 🎉")
        else:
            messagebox.showwarning("Wrong!", f"Better luck next time, {current_player}!")

        messagebox.showinfo("Answer", f"The correct word was: {self.picked_word}")

        self.clear_screen()
        self.show_continue_screen()

    def show_continue_screen(self):
        tk.Label(self.root, text=f"Scores:\n{self.p1name.get()}: {self.p1score}\n{self.p2name.get()}: {self.p2score}",
                 font=("Arial", 14), bg="#f0f8ff").pack(pady=20)

        tk.Button(self.root, text="Continue", command=self.continue_game, bg="green", fg="white").pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.end_game, bg="red", fg="white").pack(pady=10)

    def continue_game(self):
        self.turn += 1
        self.clear_screen()
        self.next_round()

    def end_game(self):
        self.clear_screen()
        winner_text = "Draw! Well played!" if self.p1score == self.p2score else \
                      f"Winner is {self.p1name.get()}" if self.p1score > self.p2score else \
                      f"Winner is {self.p2name.get()}"

        tk.Label(self.root, text="Final Scores", font=("Arial", 16), bg="#f0f8ff").pack(pady=10)
        tk.Label(self.root, text=f"{self.p1name.get()}: {self.p1score}\n{self.p2name.get()}: {self.p2score}",
                 font=("Arial", 14), bg="#f0f8ff").pack(pady=20)
        tk.Label(self.root, text=winner_text, font=("Arial", 16), fg="purple", bg="#f0f8ff").pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Driver code
if __name__ == '__main__':
    root = tk.Tk()
    game = WordGameGUI(root)
    root.mainloop()
