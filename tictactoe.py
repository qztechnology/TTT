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
    X_bs = [[X,EMPTY,EMPTY],
        [EMPTY, X, EMPTY],
        [EMPTY, EMPTY, X]]
    X_s = [[EMPTY,EMPTY,X],
            [EMPTY, X, EMPTY],
            [X, EMPTY, EMPTY]]
    O_bs = [[O,EMPTY,EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, O]]
    O_s = [[EMPTY,EMPTY,O],
            [EMPTY, O, EMPTY],
            [O, EMPTY, EMPTY]]
    
    # Row winners
    for i in range(3):
        if board[i].count(X) == 3:
            return X
        elif board[i].count(O) == 3:
            return O
        
    # Column winners
    column = []
    for j in range(3):
      column = [board[i][j] for i in range(3)]
      if column[0] != EMPTY and all(c == column[0] for c in column):
        print(f"{column[0]} WINS!")
        
    # Diagonal winners
    if board == X_bs or board == X_s:
      return X
    elif board == O_bs or board == O_s:
      return O
    

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
