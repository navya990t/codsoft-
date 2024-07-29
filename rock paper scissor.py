import tkinter as tk
from tkinter import messagebox
import random
from tkinter import Label

player_score = 0
computer_score = 0

def computerchoice():
    choices=["ROCK","PAPER","SCISSORS"]
    return random.choice(choices)
def playergame(choice):
    global player_score,computer_score
    system=computerchoice()
    result=play(choice.upper(),system)
    update_result(result)
    update_scores
def play(player,system):
    if player==system:
        return "tie!"
    elif(player=="ROCK" and system=="SCISSORS") or (player=="PAPER" and system=="ROCK")or (player=="SCISSORS" and system=="PAPER"):
        return "You Won the game!"
        player_score+=1
    else:
        return "Computer Won!"
        computer_score+=1
    update_scores()
    update_result(result)
def update_result(result):
    result_var.set(result)

def update_scores():
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

r=tk.Tk()
r.title("Rock Paper Scissors Game")

header_label = tk.Label(r, text="Rock Paper Scissors", font=('Helvetica', 18))
header_label.pack(pady=20)

score_label = tk.Label(r, text="Player: 0  Computer: 0", font=('Helvetica', 14))
score_label.pack() 


result_var=tk.StringVar()
res_entry=tk.Entry(r,textvariable=result_var,font=('Helvetica',14))
res_entry.pack(pady=30)
frame=tk.Frame(r)
frame.pack(pady=20)
tk.Button(frame, text="Rock", width=10, command=lambda: playergame('Rock')).pack(side=tk.LEFT, padx=10)
tk.Button(frame, text="Paper", width=10, command=lambda: playergame('Paper')).pack(side=tk.LEFT, padx=10)
tk.Button(frame, text="Scissors", width=10, command=lambda: playergame('Scissors')).pack(side=tk.LEFT, padx=10)
r.mainloop()


