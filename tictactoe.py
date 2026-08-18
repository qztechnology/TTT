"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    # Cell limit counter
    counter = 8
    
    # The first player is X
    if board == initial_state():
        return "X"
    
    # Scan the all board to check how EMPTY
    for row in board:
        for cell in row:
            if cell != EMPTY:
                counter -= 1
    
    # based on the EMPTIES in the board select the next player
    if counter % 2 == 0:
      print(f"player X")
    else:
      print(f"player O")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions = []

    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == EMPTY:
                free_cell = (i,j)
                actions.append(free_cell)
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_copy = copy.deepcopy(board)

    possible_actions = []

    # Coordinates of current board
    for i,row in enumerate(board_copy):
           for j,cell in enumerate(row):
                if cell == EMPTY:
                    free_cell = (i,j)
                    possible_actions.append(free_cell)

    if action not in possible_actions:
          raise Exception("Action not valid")
    else:
        return possible_actions.remove(action)
     

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    X_counter = 0
    O_counter = 0
    
    # Row winners
    for i in range(3):
        if board[i].count(X) == 3:
            print("X WINS!")
            break
        elif board[i].count(O) == 3:
            print("O WINS!")
            break
        
    # Column winners
    for j in range(3):
          match j:
            case 0:
              if board[i][0] == X:          
                X_counter += 1
                if X_counter == 3:
                  print("X WINS!")
                  break
              if board[i][j] == O:          
                O_counter += 1
                if O_counter == 3:
                  print("O WINS!")
                  break
            case 1:
              if board[i][j] == X:          
                X_counter += 1
                if X_counter == 3:
                  print("X WINS!")
                  break
              if board[i][j] == O:          
                O_counter += 1
                if O_counter == 3:
                  print("O WINS!")
                  break
            case 2:
              if board[i][j] == X:          
                X_counter += 1
                if X_counter == 3:
                  print("X WINS!")
                  break
              if board[i][j] == O:          
                O_counter += 1
                if O_counter == 3:
                  print("O WINS!")
                  break
              
    # Diagonal winners
    """if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
            print("X WINS!")

    
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
            print("O WINS!")"""
    



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


def check_matrix():
    """
    Returns the matrix state.
    """
    return True
