from typing import List

def part1(pattern : List[str], slope : tuple) -> int:
    trees = 0
    down, right = 0, 0
    # I would argue the iterative "raw-loop" here is better than using a functional approach
    while (down < len(pattern)):
        # note that the pattern extends to the right infinitely, meaning the cols
        # of each row extend following modular arithmetic col % N, where N is # of cols
        if pattern[down][right % len(pattern[down])] == "#":
            trees += 1
        down += slope[0]
        right += slope[1]
    return trees

def part2(pattern : List[str], slopes : List[tuple]) -> int:
    import math
    # https://www.python.org/dev/peps/pep-0289/
    return math.prod(part1(pattern, slope) for slope in slopes) # generator exression

if __name__ == "__main__":
    pattern = open("../input.txt").read().splitlines() # M x N grid
    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)] # convention is rows down, columns right
    print("Part 1:", part1(pattern, slopes[1])) # O(M) time, O(1) space
    print("Part 2:", part2(pattern, slopes)) # O(M) time and O(1) space