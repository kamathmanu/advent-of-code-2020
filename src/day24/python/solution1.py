import re
from collections import Counter
from typing import List

# regex + complex numbers inspired solution

def simulate(insn_seq : List[str]):
    r = re.compile(r'[ns]?[we]')
    dirs = {'e': 1, 'w': -1, 'ne': 1 + 1j, 'se': 1 - 1j, 'nw': -1 + 1j, 'sw': -1 - 1j}


    # keep state of only tiles that are black - saves space
    flips = Counter(sum(dirs[m.group(0)] for m in r.finditer(line)) for line in insn_seq)
    black = {k for k,v in flips.items() if v & 1}
    pt1 = len(black)
    for _ in range(100):
        counts = Counter(pt + d for pt in black for d in dirs.values())
        black = set(k for k, v in counts.items() if v == 2 or k in black and v == 1)
    pt2 = len(black)
    return pt1, pt2 

if __name__ == "__main__":
    insns = open('../input.txt').read().splitlines()
    part1, part2 = simulate(insns)
    print("Part 1:", part1) # 332
    print("Part 2:", part2) # 3900