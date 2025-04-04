"""
2025-04-04-금요일
"""


def solution(n):
    numbers, result = [], []
    count = 1

    for _ in range(n):
        value = int(input())
        while count <= value:
            numbers.append(count)
            result.append("+")
            count += 1

        if numbers[-1] == value:
            numbers.pop()
            result.append("-")
        else:
            return ["NO"]

    return result


n = int(input())

for x in solution(n):
    print(x)