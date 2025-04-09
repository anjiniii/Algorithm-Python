"""
2025-04-09-수요일
"""


# 1차 시도 - 틀림
def solution():
    n = int(input())
    pattern = input()
    left = pattern[:pattern.index("*")]
    right = pattern[pattern.index("*")+1:]

    for _ in range(n):
        string = input()
        if string.startswith(left) and string.endswith(right):
            print("DA")
        else:
            print("NE")


# 2차 시도
def solution2():
    n = int(input())
    pattern = input()
    left, right = pattern.split("*")

    for _ in range(n):
        string = input()
        if len(string) >= len(pattern) - 1 and string.startswith(left) and string.endswith(right):
            print("DA")
        else:
            print("NE")


solution2()