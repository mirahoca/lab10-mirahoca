# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # 1. Make an empty stack to hold numbers
    # 2. Go through each token left to right
    # 3. If the token is a number, convert it to int and push it on the stack
    # 4. If the token is an operator, pop two numbers
    # The first pop is the right operand (b), the second pop is the left operand (a). Then a operator b
    # 5. For "/", use int(a / b) so it goes toward zero
    # 6. When the tokens run out, the one value left on the stack is the answer

    stack = []
    for tok in tokens:
        if tok in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[0]
    pass


def decode_string(s):
    # Outline:
    # 1. Keep a stack of (previous_string, repeat_count) pairs
    # 2. Keep two working variables: 'current' and 'num'
    # 3. Digit: add it to 'num' (num = num * 10 + digit) so "12[a]" works
    # 4. "[": push (current, num) on the stack, then reset current = "" and num = 0
    # 5. "]": pop (prev, k) and set current = prev + current * k
    # 6. Any other character (a letter): append it to 'current'
    # 7. 'current' holds the fully decoded string

    stack = []
    current = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((current, num))
            current = ""
            num = 0
        elif ch == "]":
            prev, k = stack.pop()
            current = prev + current * k
        else:
            current += ch
    return current
    pass


def daily_temperatures(temps):
    # Outline:
    # 1. Make a result list of zeros, same length as temps (0 = no warmer day)
    # 2. Make a stack of indeces of days still waiting for a warmer day
    # The temperatures are in decreasing order from bottom to top
    # 3. For each day i, while the stack is not empty and temps[i] is warmer than
    # the temperature at the index on top of the stack:
    #       pop that index j and set result[j] = i - j
    # 4. Push i onto the stack
    # 5. Days left on the stack at the end never found a warmer day, so they stay 0
    # 6. Each index is pushed and popped at most once, so this runs in O(n)

    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result
 
    pass


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
