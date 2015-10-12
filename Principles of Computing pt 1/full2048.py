"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    shifted = shift(line)
    shifted.append(0)
    merged = [0]*len(line)
    merged_idx = 0
    shifted_idx = 0
    while shifted_idx < (len(shifted)-1):
        if shifted[shifted_idx] == shifted[shifted_idx+1]:
            merged[merged_idx] = shifted[shifted_idx]*2
            shifted_idx += 2
        elif shifted[shifted_idx] != shifted[shifted_idx+1]:
            merged[merged_idx] = shifted[shifted_idx]
            shifted_idx += 1
        merged_idx += 1     
    return merged
    
def shift(line):
    """
    Helper method that shifts non-zero values to lower idices
    """
    result = [0]*len(line)
    result_idx = 0
    for idx in range(len(line)):
        if line[idx] != 0:
            result[result_idx] = line[idx]
            result_idx += 1
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = [[0] * self._grid_width for dummy_idx in xrange(self._grid_height)]
        #creates initial row dictionary
        self._initial = {
            UP : [[0, element] for element in range(self.get_grid_width())],
            DOWN : [[self.get_grid_height() - 1, element] for element in range(self.get_grid_width())],
            LEFT : [[element, 0] for element in range(self.get_grid_height())],
            RIGHT : [[element, self.get_grid_width() - 1] for element in range(self.get_grid_height())]
        }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.__init__(self._grid_height, self._grid_width)
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial = self._initial[direction]
        temp_list = []
        
        if(direction == UP):
            self.move_helper(initial, direction, temp_list, self.get_grid_height())
        elif(direction == DOWN):
            self.move_helper(initial, direction, temp_list, self.get_grid_height())
        elif(direction == LEFT):
            self.move_helper(initial, direction, temp_list, self.get_grid_width())
        elif(direction == RIGHT):
            self.move_helper(initial, direction, temp_list, self.get_grid_width())
        else:
            print "Invalid direction"
            
    def move_helper(self, initial, direction, temp_list, row_or_col_size):
        """
        Helper method for executing the move function
        """
        before_move = str(self._grid)
            
        for element in initial:
            temp_list.append(element)
                
            for dummy_idx in range(1, row_or_col_size):
                temp_list.append([x + y for x, y in zip(temp_list[-1], OFFSETS[direction])])
                    
            indices = []
                
            for index in temp_list:
                indices.append(self.get_tile(index[0], index[1]))
                    
            merged = merge(indices)
                
            for index_x, index_y in zip(merged, temp_list):
                self.set_tile(index_y[0], index_y[1], index_x)
                    
            temp_list = []
                
        after_move = str(self._grid)
        if before_move != after_move:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = self.get_rand_row()
        col = self.get_rand_col()
        while not self.is_empty(row, col):
            row = self.get_rand_row()
            col = self.get_rand_col()
        self.set_tile(row, col, self.new_tile_val())

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        tile = self._grid[row][col]
        return tile

    def is_empty(self, row, col):
        """
        Checks to see if selected tile is empty
        Returns True if empty, False if not
        """
        tile = self.get_tile(row, col)
        if tile == 0:
            return True
        else:
            return False
    
    def get_rand_row(self):
        """
        Returns random row relative to grid height
        """
        row = int(random.randrange(self._grid_height))
        return row
    
    def get_rand_col(self):
        """
        Returns random column relative to grid width
        """
        col = int(random.randrange(self._grid_width))
        return col
    
    def new_tile_val(self):
        """
        Generates and returns value of a new tile
        """
        probability = int(random.randrange(11))
        new_tile_val = 0
        if probability <= 9:
            new_tile_val = 2
        else:
            new_tile_val = 4
        return new_tile_val