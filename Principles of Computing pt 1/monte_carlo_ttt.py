"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function plays a game starting with the given player by making random moves,
    alternating between players. The function returns when the game is over.
    """
    curplayer = player
    winner = None
    empty_squares = board.get_empty_squares()
    while winner == None and len(empty_squares) > 0:
        
        move_choice = random.choice(empty_squares)
        board.move(move_choice[0], move_choice[1], curplayer)
        winner = board.check_win()
        curplayer = provided.switch_player(curplayer)
        
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is
    The function scores the completed board and updates the scores grid
    """
    current_board = board.clone()
    winner = current_board.check_win()
    
    for row in range(current_board.get_dim()):
        for col in range(current_board.get_dim()):
            if winner == provided.DRAW:
                scores[row][col] += 0
            elif winner == player and board.square(row,col) == player:
                scores[row][col] += SCORE_CURRENT
            elif winner == player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] -= SCORE_OTHER
            elif winner != player and board.square(row,col) == player:
                scores[row][col] -= SCORE_CURRENT
            elif winner != player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] += SCORE_OTHER
            elif board.square(row, col) == provided.EMPTY:
                scores[row][col] -= 0.0

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores
    The function finds all of the empty squares with the maximum score 
    and randomly returns one of them as a (row, column) tuple.
    """
    max_score = -1000
    
    for col in range(board.get_dim()):
            for row in range(board.get_dim()):
                if scores[row][col] >  max_score and board.square(row, col) == provided.EMPTY:
                    
                    max_score = scores[row][col]
                    
    # find empty squares with max score                
    empty_squares = board.get_empty_squares()
    move_list = []
    for square in empty_squares:
        if scores[square[0]][square[1]] == max_score:
            move_list.append(square)

    row, col = move_list[random.randrange(0,len(move_list))] 
    return row, col

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, 
    and the number of trials to run. The function returns a move for the machine 
    player in the form of a (row, column) tuple.
    """
    grid_size = board.get_dim()
    scores_grid = [[0 for row in range(grid_size)] for col in range(grid_size)]
    
    for dummy_trial in range(trials):
        current_board = board.clone()
        mc_trial(current_board, player)
        mc_update_scores(scores_grid, current_board, player)
    
    row, col = get_best_move(board, scores_grid)
    return row, col


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
