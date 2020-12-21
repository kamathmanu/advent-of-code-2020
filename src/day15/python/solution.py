from collections import Counter
from typing import Dict, List
import time

def play_turn(said: Dict[int, int], last_number, turn: int) -> int:
    most_recent = said[last_number]
    spoken = 0 if most_recent[0] == most_recent[1] else (most_recent[1] - most_recent[0])
    said[spoken] = [turn, turn] if spoken not in said else [said[spoken][1], turn]
    return spoken

def determine_nth(starting_nums : List[int], N) -> int:
    # Dictionary generators!
    previously_seen = {i: [0,0] for i in starting_nums} # key is number spoken, val[0] and val[1] is 2nd and 1st most recent time number is seen respectively
    for turn in range(1, N + 1):
        if turn <= len(starting_nums):
            previously_seen[starting_nums[turn-1]][0] = turn
            previously_seen[starting_nums[turn-1]][1] = turn
            last_number = starting_nums[turn-1]
        else:
            last_number = play_turn(previously_seen, last_number, turn)
    return last_number


if __name__ == "__main__":
    starting_nums = [18,8,0,5,4,1,20]    
    
    print("Part 1:", determine_nth(starting_nums, 2020))
    start_time = time.time()
    print("Part 2:", determine_nth(starting_nums, 30000000)) 
    print("Part 2 w/hash map took {0:.2f} seconds", time.time() - start_time)