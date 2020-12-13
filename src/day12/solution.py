
from typing import List

def manhattan_distance(directions : List[str]):
    net_x, net_y, net_rotated = 0, 0, 0
    for direction in directions:
        action, val = direction[0], int(direction[1:])
        if action == 'N':
            net_y += val
        elif action == 'S':
            net_y -= val
        elif action == 'E':
            net_x += val
        elif action == 'W':
            net_x -= val
        elif action == 'L':
            net_rotated += (val // 90)
            net_rotated %= 4
        elif action == 'R':
            net_rotated += (-val // 90)
            net_rotated %= 4
        elif action == 'F':
            # move based on which pole we are facing
            if net_rotated == 0:
                net_x += val
            elif net_rotated == 2:
                net_x -= val
            elif net_rotated == 1:
                net_y += val
            elif net_rotated == 3:
                net_y -= val
        else:
            # throw an error?
            pass
    return abs(net_x) + abs(net_y)

def manhattan_distance_waypoint(directions):
    # complex numbers can be used to simulate vectors/cartesian coordinates well
    ship_position = 0 + 0j
    waypoint_position = 10 + 1j

    offset = {'E': 1 + 0j, 'W': -1 + 0j, 'N': 0 + 1j, 'S': 0 - 1j}
    rot = {'L': 0 + 1j, 'R': 0 - 1j}

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

def part1(directions : List[str]) :
    # start at 0,0
    # consider x,y coordinate E = +x, W = -x, N = +y, S = -y
    # BIG ASSUMPTION about rotation: we only rotate by multiple of 90 degrees
    # consider rotation coordinate: L is positive axis
    # therefore if we keep track of the net rotation t so far, 0 <= t < 360, t is multiple of 90,
    # L0 : E L90 : N L180: W: L270. For right rotations we simply consider it as rotating left by a -ve degree.
    print("Part 1: ", manhattan_distance(directions))

def part2(directions : List[str]):
    print("Part 2:", manhattan_distance_waypoint(directions))


if __name__ == "__main__":
    with open('input.txt') as f:
        directions = [line.strip() for line in f]
    
    test_dirs = ['F10', 'N3', 'F7', 'R90', 'F11']
    part1(directions) # 2228
    part2(directions) 
