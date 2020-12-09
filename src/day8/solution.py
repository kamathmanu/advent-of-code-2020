# consider our input stored as a list of the command, with an extra field
# specifying if the command was visited or not. Each time we visit a command,
# we set this to true. We then traverse the list based on the command type
# if it is a jump we use the indices to travel to the next element
# if it is an acc, we go to the next element, and increment our acc variable
# if it is a nop, we go to the next element

from typing import List, Tuple

class loc():
    def __init__(self, cmd, val, visited):
        self.cmd = cmd
        self.val = val
        self.visited = visited
    def mark_visited(self):
        self.visited = True

def acc_before_cycle(code : List[loc]) -> Tuple[int, loc]:
    total_acc = 0
    idx = 0
    while (0 <= idx < len(code)):
        if code[idx].visited:
            return total_acc, code[idx] # return both the acc value and insn which started the cycle
        code[idx].mark_visited()
        cmd, val = code[idx].cmd, code[idx].val
        if cmd == "acc":
            total_acc += val
            idx += 1
        elif cmd == "nop":
            idx += 1
        elif cmd == "jmp":
            idx += val

    return total_acc, None

def acc_after_change(code : List[loc]) -> int:
    import copy
    program = copy.deepcopy(code) # create a copy so we don't pollute the original code
    idx = 0

    while True:
        acc, loop_instruction = acc_before_cycle(program)
        # print(acc, loop_instruction.cmd, loop_instruction.val)
        # break
        if loop_instruction is not None:
            program = copy.deepcopy(code) # this keeps generating copies???
            # there was a loop, keep moving till we see a nop or a jmp, try swapping and then see how that fares
            while program[idx].cmd == "acc":
                idx += 1
            
            if program[idx].cmd == "nop":
                program[idx].cmd = "jmp"
            else:
                program[idx].cmd = "nop"
            idx += 1
        else:
            break
    return acc

def part1(code):
    acc, bad_insn = acc_before_cycle(code)
    return acc

def part2(code):
    final_acc = acc_after_change(code)
    return final_acc

if __name__ == "__main__":
    import copy
    # O(N) time and space (since our implicit boolean fields count as auxilliary space)
    with open("input.txt") as f:
        code = [loc(line.split()[0], int(line.split()[1]), False) for line in f]
    # TODO: analyze complexities, also improve the space in Pt 2 due to excessive copies???
    print(part1(copy.deepcopy(code)))
    print(part2(code))
