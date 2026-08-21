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
        return X
    
    # Scan the all board to check how EMPTY
    for row in board:
        for cell in row:
            if cell != EMPTY:
                counter -= 1
    
    # based on the EMPTIES in the board select the next player
    if counter % 2 == 0:
      return X
    else:
      return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions = set()

    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == EMPTY:
                free_cell = (i,j)
                actions.add(free_cell)
    
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
        if player(board) == X:
          board_copy[action[0]][action[1]] = X
        else:
          board_copy[action[0]][action[1]] = O
        possible_actions.remove(action)
        return board_copy
     

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
        return column[0]
    else:
        None
        
    # Diagonal winners
    diagonal_1 = []
    for i in range(3):
      diagonal_1 = [board[i][i] for i in range(3)]
      if diagonal_1[0] != EMPTY and all(d == diagonal_1[0] for d in diagonal_1):        
        return diagonal_1[0]
    
    diagonal_2 = []
    for i in range(3):
      diagonal_2 = [board[i][2 - i] for i in range(3)]
      if diagonal_2[0] != EMPTY and all(d == diagonal_2[0] for d in diagonal_2):
        return diagonal_2[0]
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    occupied_cell = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                occupied_cell += 1
    
    if occupied_cell == 9 or winner(board) != None:
        return True
    else:
        return False
    
         
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if terminal(board) == True:
        match winner(board):
            case "X": 
                return 1
            case "O": 
                return -1
            case None:
                return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Exit the game if is a terminal board
    if terminal(board) == True:
        return None
    else:
        best_action = ()
        vx = -math.inf
        vo = math.inf
        for action in actions(board):
            if player(board) == X:
                v = min_value(result(board,action))
                if v >= vx:
                    vx = v
                    best_action = action
                else:
                    continue
            elif player(board) == O:
                v = max_value(result(board,action))
                if v <= vo:
                    vo = v
                    best_action = action
                else:
                    continue
        return best_action
            
            
def check_matrix():
    """
    Returns the matrix state.
    """
    return True


def max_value(board):
    """
    Returns max possible value
    """  
    v = -math.inf
    
    if terminal(board) == True:
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v


def min_value(board):
    """
    Returns min possible value
    """
    v = math.inf
    
    if terminal(board) == True:
        return utility(board)
        
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v