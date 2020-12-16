from typing import List

# again maybe I'm yet to deeply understand (idiomatic) functional programming
# but I think it's usually best to borrow things from both words. At least when it
# comes to operations like map, reduce, filter: I think those operations should not
# be used if the code is not made more expressive. Hence the reduce inside the loop
# (we are 'reducing the str of multiple answers per group) and not for counts.

def part1(groups : List[List[str]]) -> int:
    from functools import reduce
    counts = 0
    for group in groups:
        # join the two string for each person and convert to a set to get unique characters
        counts += len(set(reduce(lambda x,y: x + y, group, "")))
    return counts

def unanimous_answers(group : List[str]) -> int:
    from functools import reduce
    from collections import Counter
    # each answer gets uniqified to remove duplicate answers by a person
    answers_per_person = (reduce(lambda ch1, ch2: ch1 + ch2, set(answer), "") for answer in group)
    # we want to check if all people have answered a question, so use a hashmap
    # then multiply the number of unanimous answers per person by the size of the group
    answer_freq = Counter(reduce(lambda a, b: a + b, answers_per_person, ""))
    return len(list(filter(lambda k: answer_freq[k] == len(group), answer_freq)))
    


def part2(groups : List[List[str]]) -> int:
    from functools import reduce
    # counts_per_group = (unanimous_answers(group) for group in groups)
    # print(counts_per_group)
    # reduce(sum, counts_per_group)
    count = 0
    for group in groups:
        count += unanimous_answers(group)
    return count
    

if __name__ == "__main__":
    # NOTE!: MUST TRIM the trailing whitespace at end to include last group in part 2
    input = [entry.split('\n') for entry in open('../input.txt').read().rstrip('\n\n').split('\n\n')] 
    print("Part 1:", part1(input)) # O(N) time and space, N is # of groups.
    print("Part 2:", part2(input))
    # REVIEW SET ALGOS! See C++ version.