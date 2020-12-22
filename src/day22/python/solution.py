import copy
from typing import List, Tuple

def calculate_score(winning_hand : List[int]) -> int:
    points = [a * b for a,b in zip(winning_hand, list(range(len(winning_hand), 0, -1)))]
    return sum(points)

def draw(p1 : List[int], p2: List[int]) -> List[int]:
    p1_deck = copy.deepcopy(p1)
    p2_deck = copy.deepcopy(p2)

    while p1_deck and p2_deck:
        p1_draw = p1_deck.pop(0)
        p2_draw = p2_deck.pop(0)

        if p1_draw >= p2_draw:
            p1_deck.extend([p1_draw, p2_draw])
        else:
            p2_deck.extend([p2_draw, p1_draw])
    
    winning_hand = p1_deck if p1_deck else p2_deck
    return winning_hand

def play(p1 : List[int], p2: List[int]) -> int:
    winning_hand = draw(p1, p2)
    return (calculate_score(winning_hand))

def draw_recursive(p1 : List[int], p2: List[int]) -> Tuple:
    p1_records = []
    p2_records = []

    while p1 and p2:
        # Keep records of configurations
        if (p1 in p1_records) or (p2 in p2_records):
            return 1, p1
        p1_records.append(p1)
        p2_records.append(p2)

        # Draw cards and battle
        p1_draw = p1[0]
        p2_draw = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]
        
        if p1_draw <= len(p1) and p2_draw <= len(p2):
            c_p1 = copy.deepcopy(p1)[:p1_draw]
            c_p2 = copy.deepcopy(p2)[:p2_draw]
            winner, _ = draw_recursive(c_p1, c_p2)
            if winner == 1:
                p1 += [p1_draw, p2_draw]
            else:
                p2 += [p2_draw, p1_draw]

        elif p1_draw > p2_draw:
            p1 += [p1_draw, p2_draw]
        else:
            p2 += [p2_draw, p1_draw]

    return (1, p1) if p1 else (2, p2)

def play_recursive(p1 : List[int], p2: List[int]) -> int:
    _, winning_hand = draw_recursive(p1, p2)
    return calculate_score(winning_hand)

if __name__ == "__main__":
    input = open('../input.txt').read().splitlines()
    split_idx = input.index('')
    p1, p2 = [int(x) for x in input[1:split_idx]], [int(x) for x in input[split_idx+2:]]
    print("Part 1:", play(p1, p2))
    print("Part 2:", play_recursive(p1, p2))