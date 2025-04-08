"""
2025-04-08-화요일
stack
"""

arr = input()
stack = []
result = 0

for i, x in enumerate(arr):
    if x == "(":
        stack.append("(")
    elif arr[i - 1] == "(" and x == ")":
        stack.pop()
        result += len(stack)
    else:
        stack.pop()
        result += 1

print(result)