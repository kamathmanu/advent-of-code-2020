# we want the number of valid passwords, i.e. number of lines that obey the rules

from collections import Counter

# get the two numbers, the character and the string password respectively from the line
def getTokens(line) -> (int, int, str, str):
    tokens = line.split()
    (num1, num2) = map(int, tokens[0].split("-"))
    ch = tokens[1][0] # since we know it's a single char
    psswd = tokens[-1]
    return (num1, num2, ch, psswd)

def isValidPart1(line) -> bool:
    lower, upper, ch, password = getTokens(line)
    return lower <= Counter(password)[ch] <= upper

def isValidPart2(line) -> bool:
    pos_a, pos_b, ch, password = getTokens(line)
    # get the characters of the indexes (modify them to zero based)
    # in the password, check only one of them = ch
    from operator import xor
    return xor((password[pos_a - 1] == ch), (password[pos_b - 1] == ch)) 

if __name__ == "__main__":
    # filter out valid lines and return how many of them are there
    # O(N) time and space, N is the number of passwords
    with open("input.txt") as f:
        print("Part 1: ", len(list(filter(isValidPart1, f))))
    
    with open("input.txt") as f:
        print("Part 2: ", len(list(filter(isValidPart2, f))))
