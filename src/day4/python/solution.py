from typing import List
# Parsing is definitely the most challenging part of this problem

def simple_valid(passport : str) -> bool:
    fields = set([e.split(':')[0] for e in passport.split()])
    return (len(fields) == 8) or (len(fields) == 7 and "cid" not in fields)

def part1(passports : List[str]) -> int:
    return len(list(filter(simple_valid, passports)))

def value_valid(passport: str) -> int:
    import re
    # as opposed to a set, we just use a dict instead to validate both keys and values
    # note the power of lambdas!
    valid = {
        "byr" : lambda val: 1920 <= int(val) <= 2002,
        "iyr" : lambda val: 2010 <= int(val) <= 2020,
        "eyr" : lambda val: 2020 <= int(val) <= 2030,
        "hgt" : lambda val: (val[-2:] == "cm" and 150 <= int(val[:-2]) <= 193) or (val[-2:] == "in" and 59 <= int(val[:-2]) <= 76),
        "hcl" : lambda val: re.fullmatch(r"#[\da-f]{6}", val),
        "ecl" : lambda val: val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid" : lambda val: re.fullmatch(r"[\d]{9}", val)
    }

    fields = dict(e.split(':') for e in passport.split())
    # check both the number of valid fields and their values
    valid_len = len(fields) == 8 or (len(fields) == 7 and "cid" not in fields)
    if not valid_len: return False

    for key, value in fields.items():
        if key != "cid" and not valid[key](value):
            return False
    return True

def part2(passports : List[str]) -> int:
    return len(list(filter(value_valid, passports)))


if __name__ == "__main__":
    # we can exploit the fact that the way the input is broken up, 
    # two newline characters delimit a given passport.
    passports = open("../input.txt").read().split("\n\n")
    # print(passports[0])
    print("Part 1:", part1(passports))
    print("Part 2:", part2(passports))
    pass