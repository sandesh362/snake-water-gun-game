import random
import tkinter as tk
from tkinter import messagebox

# Game choices and corresponding keys
choices = {"a": "snake", "s": "water", "d": "gun"}  # Player 1
choices_p2 = {"1": "snake", "2": "water", "3": "gun"}  # Player 2
emoji_dict = {"snake": "🐍", "water": "💧", "gun": "🔫"}

player1_choice = None
player2_choice = None

# Determine the winner
def get_winner(player, computer):
    if player == computer:
        return "🤝 It's a Tie!"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "🎉 Player 1 Wins!"
    else:
        return "😢 Player 2 Wins!"

# Capture player choices
def key_pressed(event):
    global player1_choice, player2_choice
    key = event.char.lower()
    
    if key in choices and player1_choice is None:
        player1_choice = choices[key]
        p1_label.config(text="✅ Player 1 has chosen!")
    elif key in choices_p2 and player2_choice is None:
        player2_choice = choices_p2[key]
        p2_label.config(text="✅ Player 2 has chosen!")
    
    if player1_choice and player2_choice:
        reveal_winner()

# Reveal choices and winner
def reveal_winner():
    result = get_winner(player1_choice, player2_choice)
    result_label.config(text=f"Player 1: {emoji_dict[player1_choice]}\nPlayer 2: {emoji_dict[player2_choice]}\n{result}")

# Reset game
def reset_game():
    global player1_choice, player2_choice
    player1_choice, player2_choice = None, None
    print("Player 1:ss A (🐍), S (💧), or  PreD (🔫)")
    print("Player 2: Press 1 (🐍), 2 (💧), or 3 (🔫)")
    # p1_label.config(text="Player 1: Press A (🐍), S (💧), or D (🔫)")
    # p2_label.config(text="Player 2: Press 1 (🐍), 2 (💧), or 3 (🔫)")

    p1_label.config(text="Waiting for Player 1...")
    p2_label.config(text="Waiting for Player 2...")
    result_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Snake-Water-Gun PvP")
root.geometry("400x400")
root.configure(bg="#2C3E50")
root.bind("<Key>", key_pressed)

title_label = tk.Label(root, text="🔥 Snake-Water-Gun PvP 🔥 ", font=("Times New Roman", 19, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=12)

#extra space
p1_label = tk.Label(root, text=" ", font=("Arial", 1, "bold"), bg="#2C3E50", fg="white")
p1_label.pack(pady=6)


p1_label = tk.Label(root, text="Player 1: Press A (🐍), S (💧), or D (🔫)", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white")
p1_label.pack(pady=8)

p2_label = tk.Label(root, text="Player 2: Press 1 (🐍), 2 (💧), or 3 (🔫)", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white")
p2_label.pack(pady=8)

p1_label = tk.Label(root, text="Waiting for Player 1...", font=("Arial", 12, ), bg="#2C3E50", fg="white")
p1_label.pack(pady=5)

p2_label = tk.Label(root, text="Waiting for Player 2...", font=("Arial", 12,), bg="#2C3E50", fg="white")
p2_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
result_label.pack(pady=20)

reset_btn = tk.Button(root, text="Reset", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=reset_game)
reset_btn.pack()

root.mainloop()
