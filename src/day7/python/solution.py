from typing import Dict,List

# Part 1 has a DFS/dynamic-programming pattern.

# Parse as a dictionary; keys are the corresponding colour of bag
# each key's value is a List of strings in the format '<#> <colour>'
# The number of bags may be useful for part2
def parse_input(filename) -> Dict[str, List[str]]:
    rules_list = open(filename).read().splitlines()
    valid_rules = dict()
    # the challenge is to extract the colours and values here properly
    # regex is the best bet here
    import re
    # if we observe the input.txt file we find the following structure for every rule:
    # a colour(+value) entry is separated by bag, bags or bags contain. There are no grammatical
    # connecting words (conjunctions etc), but there are commas and periods.
    for rule in rules_list:
        # a hack below - the regexp works for the general case, but for the special case 
        # "bags contain no other bags" it will split to the token 'her', so we filter that out too.
        tokens = list(filter(lambda token: token and token != 'her', re.split(r" bag[s contain,.]*", rule)))
        key, val = tokens[0], tokens[1:]
        valid_rules[key] = val
    return valid_rules

def dfs(rules, primary_bag, memo) -> bool:
    # Base case(s):
    # The key's colour has an empty list (contains no other bags) - return False
    result = False
    if not rules[primary_bag]:
        memo[primary_bag] = result
        return result
    
    # check memoized
    if memo[primary_bag] is not None:
        return memo[primary_bag]
    # otherwise recurse and set the memo
    result = False
    for entry in rules[primary_bag]:
        colour = entry.split(" ", 1)[1]

        # print(primary_bag, ":", colour) # use to debug DFS + memoization

        # If the colour is "shiny gold", then we've found our result 
        # and we can mark that the primary_bag can hold a shiny gold bag
        if colour == 'shiny gold':
            result = True
        # otherwise we recurse on that colour
        else:
            result = dfs(rules, colour, memo)
        if result is True: # if we've found a shiny gold, then mark the primary_bag's DFS as true
            memo[primary_bag] = result
            return result

    memo[primary_bag] = result
    return result

def part1(rules : Dict[str, List[str]]):
    # Traverse through the keys - performing a DFS for each colour *value* in the dictionary
    # Memoize this to preserve runtime efficiency - Top-down DP approach
    memo = dict(zip(rules.keys(), (None for _ in range(len(rules))) )) # generator for laziness??
    result = 0
    for bag in rules:
        if dfs(rules, bag, memo): # O(R) time and space, R is the # of rules
            result += 1
    print("Part 1:", result)
    return result

if __name__ == "__main__":
    # bag_rules = parse_input('../test_pt1.txt') # Expected answer = 4
    bag_rules = parse_input('../input.txt')
    count = part1(bag_rules)
    bag_rules = parse_input('../test_pt2.txt') # Expected answer = 126
    part2(bag_rules)