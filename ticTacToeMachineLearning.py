#############################################################
# A fun project to play with reinforcement machine learning
# principles.
#
# The goal is to create a tic-tac-toe game that learns how
# to play as it plays you. Alternatively, you can pla against
# an experienced machine and its history of previous games
#############################################################
import pandas as pd

current_state = dict()

def clear_board():
    print("Starting a new game")
    global current_state
    current_state = {"a1": " ",
                     "a2": " ",
                     "a3": " ",
                     "b1": " ",
                     "b2": " ",
                     "b3": " ",
                     "c1": " ",
                     "c2": " ",
                     "c3": " "
                    }


def draw_board():
    global current_state
    print("    |   |    ")
    print("  {0} | {1} | {2}  ".format(current_state["a1"], current_state["b1"], current_state["c1"]))
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print("  {0} | {1} | {2}  ".format(current_state["a2"], current_state["b2"], current_state["c2"]))
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print("  {0} | {1} | {2}  ".format(current_state["a3"], current_state["b3"], current_state["c3"]))
    print("    |   |    ")

def get_possible_moves():
    global current_state
    #############################################################
    # Get list of possible moves, represented by a space in the
    # square, which is indicated by a space in the dictionary
    #############################################################
    possible_moves = list()
    for square in list(current_state.keys()):
        if current_state[square] == " ":
            possible_moves.append(square)
    return possible_moves
    

def ask_for_move():
    global current_state
    next_move = None
    print("Squares are labeled A, B, C horizontally, and then 1, 2, 3 top to bottom")
    valid = False
    while not valid:
        print("Possible moves: {0}".format(possible_moves))
        next_move = input("What square do you want to play? ")
        next_move = next_move.lower()
        if next_move in possible_moves:
            valid = True
        else:
            print("{0} is not a valid move".format(next_move))
    return next_move

def make_move(next_move, player):
    global current_state
    current_state[next_move] = player

def check_for_winner_horizontal():
    global current_state
    if current_state["a1"] != " " and current_state["a1"] == current_state["b1"] and current_state["b1"] == current_state["c1"]: return True
    if current_state["a2"] != " " and current_state["a2"] == current_state["b2"] and current_state["b2"] == current_state["c2"]: return True
    if current_state["a3"] != " " and current_state["a3"] == current_state["b3"] and current_state["b3"] == current_state["c3"]: return True
    return False

def check_for_winner_vertical():
    global current_state
    if current_state["a1"] != " " and current_state["a1"] == current_state["a2"] and current_state["a2"] == current_state["a3"]: return True
    if current_state["b1"] != " " and current_state["b1"] == current_state["b2"] and current_state["b2"] == current_state["b3"]: return True
    if current_state["c1"] != " " and current_state["c1"] == current_state["c2"] and current_state["c2"] == current_state["c3"]: return True
    return False

def check_for_winner_diagonal():
    global current_state
    if current_state["a1"] != " " and current_state["a1"] == current_state["b2"] and current_state["b2"] == current_state["c3"]: return True
    if current_state["c1"] != " " and current_state["c1"] == current_state["b2"] and current_state["b2"] == current_state["a3"]: return True

def check_for_winner():
    if check_for_winner_horizontal() or check_for_winner_vertical() or check_for_winner_diagonal(): return True
    return False
           
#####################Main starts here#########################
done = False
while not done:
    clear_board()
    terminal_state = False
    player = None
    while player is None or player.upper() not in ('X','O'):
        player = input("Do you want to play first (X) or second (O)? Enter 'X' or 'O': ")
    player = player.upper().strip()
    while not terminal_state:
        draw_board()
        possible_moves = get_possible_moves()
        if len(possible_moves) == 0:
            print("No more moves. Game over!")
            terminal_state = True
        elif check_for_winner():
            print("We have a winner!")
            terminal_state = True
        else:
            next_move = ask_for_move()
            make_move(next_move, player)
            if player == "X":
                player = "O"
            else:
                player = "X"
    play_again = None
    while play_again is None or play_again.upper() not in ('Y','N'):
        play_again = input("Do you want to play again? Enter 'Y' or 'N': ")
    if play_again.upper() == 'N':
        done = True
print("Have a great day!")
    
