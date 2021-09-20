# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i,next))
        if next in ")]}":
            if len(opening_brackets_stack)==0:
                return i+1
            top = opening_brackets_stack.pop()
            if(top[1] =='[' and next != ']') or (top[1] =='(' and next != ')') or (top[1] =='{' and next != '}'):
                return i+1

    if(len(opening_brackets_stack)==0):
        return "Success"
    else:
        top = opening_brackets_stack.pop()[0]
        return top+1
            


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
