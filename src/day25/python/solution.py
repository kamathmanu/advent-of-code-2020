def find_loop_size(subject_number : int, target : int) -> int:
    # returns loop size
    modulus_constant = 20201227
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value = (value * subject_number) % modulus_constant
        if value == target:
            break
    return loop_size

def transform(subject_number : int, loop_size : int) -> int:
    modulus_constant = 20201227
    value = 1
    for i in range(loop_size):
        value = (value * subject_number) % modulus_constant
    return value

def part1(K_a : int, K_b : int) -> int:
    public_key_subject_number = 7
    L_a, L_b = find_loop_size(public_key_subject_number, K_a), find_loop_size(public_key_subject_number, K_b)
    return transform(K_a, L_b)

if __name__ == "__main__":
    K_a, K_b = [int(x) for x in open('../input.txt').read().splitlines()]
    print("Part 1:", part1(K_a, K_b))


