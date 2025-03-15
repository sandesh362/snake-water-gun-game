import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def get_winner(player, computer):
    """Determine the winner based on game rules."""
    if player == computer:
        return "🤝 It's a Tie!"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "🎉 You Win!"
    else:
        return "😢 Computer Wins!"

def play_with_computer():
    player_choice = player_var.get()
    if player_choice not in choices:
        messagebox.showerror("Error", "Invalid choice! Try again.")
        return
    
    computer_choice = random.choice(choices)
    result = get_winner(player_choice, computer_choice)
    
    result_label.config(text=f"You: {emoji_dict[player_choice]}\nComputer: {emoji_dict[computer_choice]}\n{result}")

def submit_player1_choice():
    global player1_choice
    player1_choice = player1_var.get()
    player1_submit_btn.config(state=tk.DISABLED)
    if player2_submit_btn['state'] == tk.DISABLED:
        play_with_friend()

def submit_player2_choice():
    global player2_choice
    player2_choice = player2_var.get()
    player2_submit_btn.config(state=tk.DISABLED)
    if player1_submit_btn['state'] == tk.DISABLED:
        play_with_friend()

def play_with_friend():
    result = get_winner(player1_choice, player2_choice)
    result_label.config(text=f"Player 1: {emoji_dict[player1_choice]}\nPlayer 2: {emoji_dict[player2_choice]}\n{result}")

def reset_pvp():
    global player1_choice, player2_choice
    player1_choice, player2_choice = None, None
    player1_submit_btn.config(state=tk.NORMAL)
    player2_submit_btn.config(state=tk.NORMAL)
    result_label.config(text="")

def switch_mode(mode):
    reset_pvp()
    if mode == "PvC":
        player1_frame.pack_forget()
        player2_frame.pack_forget()
        player_vs_computer_frame.pack()
    else:
        player_vs_computer_frame.pack_forget()
        player1_frame.pack()
        player2_frame.pack()

# Main Window
root = tk.Tk()
root.title("🎮 Snake-Water-Gun Game")
root.geometry("400x500")
root.configure(bg="#2C3E50")

# Game Choices
choices = ["snake", "water", "gun"]
emoji_dict = {"snake": "🐍", "water": "💧", "gun": "🔫"}
player1_choice, player2_choice = None, None

# Title Label
title_label = tk.Label(root, text="🔥 Snake-Water-Gun Game 🔥", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

# Mode Selection Buttons
btn_frame = tk.Frame(root, bg="#2C3E50")
btn_frame.pack()

tk.Button(btn_frame, text="Player vs Computer", font=("Arial", 12, "bold"), bg="#27AE60", fg="white", command=lambda: switch_mode("PvC")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Player vs Player", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=lambda: switch_mode("PvP")).grid(row=0, column=1, padx=5, pady=5)

# Player vs Computer Frame
player_vs_computer_frame = tk.Frame(root, bg="#2C3E50")
player_var = tk.StringVar()
tk.Label(player_vs_computer_frame, text="Choose:", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white").pack()
tk.OptionMenu(player_vs_computer_frame, player_var, *choices).pack()
tk.Button(player_vs_computer_frame, text="Play", font=("Arial", 12, "bold"), bg="#3498DB", fg="white", command=play_with_computer).pack(pady=10)

# Player vs Player Frames
player1_frame = tk.Frame(root, bg="#2C3E50")
player1_var = tk.StringVar()
tk.Label(player1_frame, text="Player 1 Choose:", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white").pack()
tk.OptionMenu(player1_frame, player1_var, *choices).pack()
player1_submit_btn = tk.Button(player1_frame, text="Submit", font=("Arial", 12, "bold"), bg="#1ABC9C", fg="white", command=submit_player1_choice)
player1_submit_btn.pack()

player2_frame = tk.Frame(root, bg="#2C3E50")
player2_var = tk.StringVar()
tk.Label(player2_frame, text="Player 2 Choose:", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white").pack()
tk.OptionMenu(player2_frame, player2_var, *choices).pack()
player2_submit_btn = tk.Button(player2_frame, text="Submit", font=("Arial", 12, "bold"), bg="#F39C12", fg="white", command=submit_player2_choice)
player2_submit_btn.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
result_label.pack(pady=20)

# Default Mode
switch_mode("PvC")

# Run the GUI
root.mainloop()
