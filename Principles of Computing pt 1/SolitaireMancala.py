"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)
        
            
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for idx in range(1, len(self._board)):
            if self._board[idx] != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == 0 or self.get_num_seeds(house_num) != house_num:
            return False
        return True

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self._board[house_num] = 0
            for idx in range(0, house_num):
                self._board[idx] += 1
        else: print "%s has no legal move" % house_num
        return self._board

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        shortest_move = 0
        for idx in range(1, len(self._board)):
            if self.is_legal_move(idx):
                shortest_move = idx
                break
        return shortest_move
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        new_board = SolitaireMancala()
        new_board.set_board(self._board)
        move_list = []
        next_move = new_board.choose_move()
        while next_move != 0:
            new_board.apply_move(next_move)
            move_list.append(next_move)
            next_move = new_board.choose_move()
        return move_list
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # Test a non-winning configuration
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    # Test a winning configuration
    win_config = [5, 0, 0, 0, 0, 0, 0]
    my_game.set_board(win_config)
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", True
    # Test legal moves
    my_game.set_board(config1)
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(0), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(2), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(3), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(4), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(6), "Expected:", False
    # Test apply legal move
    print "Testing apply_move = Computed:", my_game.apply_move(3), "Expected:", "3 has no legal move", config1
    print "Testing apply_move = Computed:", my_game.apply_move(5), "Expected:", str([1, 1, 2, 2, 4, 0, 0])
    # Test choose move
    my_game.set_board(config1)
    print "Testing choose_move = Computed:", my_game.choose_move(), "Expected:", 5
#test_mancala()


# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())