
from typing import Dict, List
# complex numbers solution
# if we have 4 different poles (i.e 2 coordinate system), using
# complex numbers are a great way to manage these and combine operations.
# for translation, they lend themselves well since the real and imag parts can
# be used for separate coordinates. They are also excellent for rotations since
# multiply complex numbers can alter the real/imaginary components.

def manhattan_distance(directions : List[str], offset: Dict[str, int], rot: Dict[str, int]) -> int:
    ship_position = 0 + 0j
    rotation_face = 1 + 0j

    for dir in directions:
        action, val = dir[0], int(dir[1:])

        if action in "EWNS":
            ship_position += val * offset[action]
        elif action in "LR":
            rotation_face *= (rot[action] ** (val // 90))
        elif action == "F":
            ship_position += val * rotation_face
    
    return int(abs(ship_position.real) + abs(ship_position.imag))


def manhattan_distance_waypoint(directions : List[str], offset: Dict[str, int], rot: Dict[str, int]):
    ship_position = 0 + 0j
    waypoint_position = 10 + 1j

    for direction in directions:
        action, val = direction[0], int(direction[1:])

        relative_distance = waypoint_position - ship_position
        if action in "EWNS":
            waypoint_position += val * offset[action]
        elif action == "F":
            ship_position += val * relative_distance
            waypoint_position += val * relative_distance
        elif action in "RL":
            relative_distance *= rot[action] ** (val // 90)
            waypoint_position = ship_position + relative_distance

    return int(abs(ship_position.real) + abs(ship_position.imag))

def part1(directions : List[str], offset: Dict[str, int], rot: Dict[str, int]) :
    print("Part 1: ", manhattan_distance(directions, offset, rot))

def part2(directions : List[str], offset: Dict[str, int], rot: Dict[str, int]):
    print("Part 2:", manhattan_distance_waypoint(directions, offset, rot))

if __name__ == "__main__":
    directions = [line.strip() for line in open('../input.txt').read().splitlines()]
    
    # offset and rotation rules for both parts
    offset = {'E': 1 + 0j, 'W': -1 + 0j, 'N': 0 + 1j, 'S': 0 - 1j}
    rot = {'L': 0 + 1j, 'R': 0 - 1j}

    # test_dirs = ['F10', 'N3', 'F7', 'R90', 'F11']
    part1(directions, offset, rot) # 2228
    part2(directions, offset, rot) # 42908
