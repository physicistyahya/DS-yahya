from tkinter import *
from tkinter import ttk
from copy import deepcopy
from tkinter import messagebox
X_WON=3
O_WON=-3
GAME_IN_PROGRESS=0
X_PLAYER = 1
O_PLAYER = 0
active_player = X_PLAYER
player_1_moves = []  # mean the
player_2_moves = []
rows_scores=[0,0,0]
columns_scores=[0,0,0]
X_O = Tk()
X_O.title("Tic Tac Toe")

cells_buttons = []

k = 0
for i in range(3):
    for j in range(3):
        cell_button = ttk.Button(X_O, text='', command=lambda button_id=k, x=i, y=j: button_click(button_id, x, y))
        cell_button.grid(row=i, column=j, sticky='snew', ipadx=40, ipady=40)
        cells_buttons.append(cell_button)
        k += 1



def apply_move(cell_id, player_symbol):
    cells_buttons[cell_id].config(text=player_symbol)
    cells_buttons[cell_id].state(['disabled'])


def player_won():
    global rows_scores,columns_scores
    for row_score in rows_scores:
        if row_score==3:
            return X_WON
        elif row_score==-3:
            return O_WON






def game_is_draw(player_1_moves, player_2_moves):
    pass


def button_click(cell_id,x,y):
    global rows_scores, columns_scores
    global active_player
    global player_1_moves
    if active_player == X_PLAYER:
        apply_move(cell_id, "X")
        player_1_moves.append((x, y))
        rows_scores[x]+=1
        columns_scores[y]+=1
        active_player = O_PLAYER
        print("Player 1 moves: {}".format(player_1_moves))
        if player_won() ==X_WON:
            print('Player one won')
        elif game_is_draw(player_1_moves,player_2_moves):
            print('draw')
    elif active_player == O_PLAYER:
        apply_move(cell_id, "O")
        player_2_moves.append((x, y))
        rows_scores[x]-=1
        columns_scores[y]-=1
        active_player = X_PLAYER
        print("Player 2 moves: {}".format(player_2_moves))
        if player_won()==O_WON:
            print('Player one won')
        elif game_is_draw(player_1_moves, player_2_moves):
            print('draw')



X_O.mainloop()
