from typing import List

def get_id(field : str):
    num = ""
    for letter in field:
        if letter == 'F' or letter == 'L':
            digit = '0'
        elif letter == 'B' or letter == 'R':
            digit = '1'
        num += digit
    return int(num,2)

def decode(boarding_pass : str) -> int:
    # run row wise and colwise binary search
    row, col = boarding_pass[:-3], boarding_pass[-3:]
    row_id, col_id = get_id(row), get_id(col)
    return row_id * 8 + col_id

def part1(boarding_passes : List[str]) -> int:
    ids = list(map(decode, boarding_passes))
    smallest, largest = min(ids), max(ids)
    print("Part 1:", largest)
    return smallest, largest, ids

def part2(ids : List[int], low : int, high : int):
    seats = set(ids)
    for i in range(low, high):
        if i not in seats:
            return i

if __name__ == "__main__":
    boarding_passes = open("../input.txt").read().splitlines()
    smallest, largest, ids = part1(boarding_passes)
    print("Part 2:", part2(ids, smallest, largest))
    # Poor space complexity, and not lazy. Revisit in C++ with a better,idiomatic solution.
