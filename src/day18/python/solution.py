from typing import Dict, List

# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

# get the tokens for the expression in the order of precedence
# basically 
def tokenize(expr: str) -> List[str]:
    rpbuf = []
    for t in expr.split():
        while t.startswith('('):
            yield '('
            t = t[1:] # prettier way to do this?
        while t.endswith(')'):
            rpbuf.append(')')
            t = t[:-1]
        if t:
            yield t
        while rpbuf:
            yield rpbuf.pop()

# Shunting-Yard algorithm for operator precedence parsing
# converts the tokens from infix to postfix (RPN) notation.
def shunting_yard(tokens : List[str], operators : Dict[str, int]) -> List[str]:
    st = []
    for token in tokens:
        if token.isdigit():
            yield token
        elif token in operators:
            while st and st[-1] in operators and operators[st[-1]] >= operators[token]:
                yield st.pop()
            st.append(token)
        elif token == '(':
            st.append(token)
        elif token == ')':
            while st and st[-1] != '(':
                yield st.pop()
            st.pop()
        else:
            raise ValueError("Unknown symbol ", token)
    while st:
        yield st.pop()

# Get tokens in RPN using Shunting Yard algo, then use a stack
# and deque to calculate the expression
def eval(expr : str, operators : Dict[str, int]) -> int:
    rpn = shunting_yard(tokenize(expr), operators)
    st = []
    for token in rpn:
        if token.isdigit():
            st.append(int(token))
        else:
            if token == '+':
                st.append(st.pop() + st.pop())
            elif token == '*':
                st.append(st.pop() * st.pop())
            else:
                raise ValueError("Undefined operator ", token)
    return st.pop()

def add_answers(exprs : List[str], operator_precedence : Dict[str, int]) -> int:
    return sum((eval(expr, operator_precedence) for expr in exprs))

if __name__ == "__main__":
    exprs = open('../input.txt').read().splitlines()
    # L to R evaluation: assign both operators equal weights
    operator_precedence = {
    "+" : 0,
    "*" : 0
    }
    print("Part 1:", add_answers(exprs, operator_precedence))
    operator_precedence["+"] = 1
    print("Part 2:", add_answers(exprs, operator_precedence))

