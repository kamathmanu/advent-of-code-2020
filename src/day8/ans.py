with open("input.txt", "r") as puzzle_input:
  base_program = [(parts[0], int(parts[1])) for parts in (line.rstrip().split(" ") for line in puzzle_input)]

def run_program(program):
  acc = 0
  idx = 0
  plen = len(program)

  while idx >= 0 and idx < plen:
    instruction = program[idx][0]
    arg = program[idx][1]

    # Since we only need to know when we start looping, overwrite the data to signify such
    program[idx] = ("inf", arg)

    if instruction == "acc": acc += arg
    elif instruction == "jmp": idx += arg
    elif instruction == "inf": break

    # Everything except jmp should move on to the next instruction
    if instruction != "jmp":
      idx += 1

  return acc, instruction

def part1():
  acc, end_instruction = run_program(base_program[:])
  return acc
  
def part2():
  change_idx = 0
  program_copy = base_program[:]
  keep_going = True
  ilen = len(program_copy)
  
  while keep_going:  
    acc, end_instruction = run_program(program_copy)

    # If the program resulted in an infinite loop, try to change a different jmp/nop
    if end_instruction == "inf":
      keep_going = True
      program_copy = base_program[:]

      while program_copy[change_idx][0] == "acc":
        change_idx += 1

      # Modify instruction and run again
      if program_copy[change_idx][0] == "nop":
        program_copy[change_idx] = ("jmp", program_copy[change_idx][1])
      else:
        program_copy[change_idx] = ("nop", program_copy[change_idx][1])

      change_idx += 1
    else:
      keep_going = False

  return acc

print("Part 1 Result: ", part1())
print("Part 2 Result: ", part2())