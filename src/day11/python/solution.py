import numpy as np
from scipy.ndimage import convolve

# Shamelessly stolen from https://github.com/metinsuloglu/AdventofCode20/blob/main/day11.py
# I find this solution to use NumPy which is what I wanted to explore. Part 1 idea was fairly easy
# to grasp and I did it myself (except for the np.where part). Part 2 I copied. 

def parse(filename : str) -> np.ndarray:
    cell_mappings = {'.': -1, 'L': 0, '#': 1}
    with open(filename) as f:
        grid = np.array([[cell_mappings[cell] for cell in row] for row in f.read().splitlines()])
    return grid

def debug_print(old_board : np.ndarray, new_board: np.ndarray, res):
    print("States:")
    print(old_board)
    print('*******')
    print(new_board)
    print("Conv result: ")
    print(res)

def simulate(grid : np.ndarray) -> np.ndarray:
    kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
    new_board = np.copy(grid)
    while True:
        old_board = np.copy(new_board)
        # get number of occupied seats next to it
        # then update the cell based on the update rules
        occupied_neighbours = convolve(np.where(new_board == 1, 1, 0), kernel, mode='constant')
        # boolean masking helps us vectorize the updates
        new_board[(new_board == 0) & (occupied_neighbours == 0)] = 1
        new_board[(new_board == 1) & (occupied_neighbours >= 4)] = 0

        # debug_print(old_board, new_board, occupied_neighbours)

        # check if the board has stabilized
        if (old_board == new_board).all(): break
    return new_board

def part1(grid : np.ndarray) -> int:
    stabilized_board = simulate(grid)
    # print(stabilized_board)
    return np.count_nonzero(stabilized_board == 1) # -1 counts as nonzero as well!

# traverse in a particular direction/offset from a given initial coord.
# do this until we find an empty or occupied seat (either stops our search for closest seat).
def closest_seat_coord(coord : tuple, offset : tuple) -> tuple:
    # coord represent a (x,y) tuple where y traverses across the columns, and x across rows.
    curr_location = (coord[0] + offset[0], coord[1] + offset[1])
    while 0 <= curr_location[0] < len(grid) and 0 <= curr_location[1] < len(grid[curr_location[0]]) and grid[curr_location] == -1:
        curr_location = (curr_location[0] + offset[0], curr_location[1] + offset[1])
    return curr_location

def simulate_directions(grid: np.ndarray) -> np.ndarray:
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    neighbours = np.array([[[closest_seat_coord((x, y), d) for d in directions]
                        for y, c in enumerate(r)] for x, r in enumerate(grid)]) # can we vectorise this?
    neighbours = np.rollaxis(neighbours + 1, -1) # rollaxis is deprecated so understand this and replace to moveaxis
    # neighbours = np.moveaxis(neighbours + 1, 0, -1)
    padded_seats = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2))

    while True:
        old_board = np.copy(grid)
        padded_seats[1:-1, 1:-1] = grid
        neighbour_vals = np.take(padded_seats, np.ravel_multi_index(neighbours, padded_seats.shape))
        res = np.sum(neighbour_vals == 1, axis=2)
        grid[(grid == 0) & (res == 0)] = 1
        grid[(grid == 1) & (res >= 5)] = 0
        if (old_board == grid).all(): break
    return grid

def part2(grid: np.ndarray) -> int:
    stabilized_board = simulate_directions(grid)
    return np.count_nonzero(stabilized_board == 1) 

if __name__ == "__main__":
    # grid = parse('../test_pt1.txt')
    grid = parse('../input.txt')
    # print(grid)
    print("Part 1:", part1(grid)) # 2283
    print("Part 2:", part2(grid)) # 2054
