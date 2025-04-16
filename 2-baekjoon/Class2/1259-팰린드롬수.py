"""
2025-04-16
"""


def solution(num):
    if len(num) == 1:
        return "yes"
    else:
        half = len(num) // 2
        left = num[:half]
        right = num[:len(num) - half - 1:-1]
        return "yes" if left == right else "no"


def solution2(num):
    if num == num[::-1]:
        return "yes"
    else:
        return "no"


while True:
    num = input()
    if num == "0":
        break
    print(solution2(num))