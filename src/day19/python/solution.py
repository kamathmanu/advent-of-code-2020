from typing import List, Dict

def match(string : str, ptr : int, rule: str):
    global ruleset
    if rule[0] == '"':
        # for single character rules
        if ptr < len(string) and string[ptr] == rule[1]:
            yield ptr+1
        return
        # piped rules
        for alt in rule.split(' | '):
            tokens = alt.split(' ', 1)
            if len(tokens) == 1:
                yield from match(string, ptr, ruleset[tokens[0]])
            else:
                for m in match(string, ptr, ruleset[tokens[0]]):
                    yield from match(string, m, tokens[1])

if __name__ == "__main__":
    rules, messages = open("../input.txt").read().split("\n\n")
    ruleset= {}
    for rule in rules.split('\n'):
        key, val = rule.split(': ')
        ruleset[key]=val
    
    valid = [1 if any(m == len(string) for m in match(string, 0, '0')) else 0 for string in messages.split('\n')]
    print(valid)
    print("Part 1:", sum(valid))
