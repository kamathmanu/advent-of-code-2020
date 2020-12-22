import numpy as np
from scipy.signal import convolve # IMPORTANT!!! See the convolve subdirectory for more info

def simulate(init_state: np.ndarray, dim: int, cycles = 6) -> int:
    """
    Create a new grid that expands the previous grid by 2 rows & cols (top & bottom),
    then perform convolution that checks gets the total neighbours for each cell in the grid.
    We then iteratively repeat this process and return the total number of active cells.
    """

    # NOTE: ndimage.convolve performs an N-dimensional convolution, meaning that the
    # image and kernel must have the same *number dimensions*. 
    # Our kernel is a 3x3x(dim) tensor, so we reshape our state grid to be a 1xMxN tensor
    next_state = init_state.reshape([1] * (dim - init_state.ndim) + list(init_state.shape)) # more Pythonic way?
    kernel = np.ones([3] * dim, dtype=np.uint8)

    for _ in range(cycles):
        neighbours = convolve(next_state, kernel) # checks each cell's neighbours over the kernel and returns the
        # how to get the count of the neighbours?
        next_state = np.pad(next_state, ((1,1),), mode='constant') & (neighbours == 4) | (neighbours == 3)

    return np.sum(next_state)


if __name__ == "__main__":
    # we can consider (#) to be a 1 and (.) to be a 0
    # input will be an M (rows) x N (cols) nd-array of 1s and 0s
    with open("../input.txt") as f:
        starting_region = np.array([list(map(lambda cell: 1 if cell == '#' else 0, row.strip())) for row in f])
    
    print("Part 1:", simulate(starting_region, 3))
    print("Part 2:", simulate(starting_region, 4))
