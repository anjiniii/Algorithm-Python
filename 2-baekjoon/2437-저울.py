"""
2025-04-10-목

"""

n = int(input())
arr = list(map(int, input().split()))


def solution2():
    arr.sort()

    target = 1
    for w in arr:
        if w <= target:
            target += w
        else:
            break

    print(target)


solution2()


def subset_sum(arr):
    result = set()
    n = len(arr)

    # << 는 비트 연산자 - n만큼 비트를 움직임 2^n
    # arr 가 가질 수 있는 모든 부분집합
    for i in range(1 << n):
        total = 0

        # i로 나타낸 부분집합에서 포함하는 값만 더하기
        # ex, 101 이라면 arr[2] + arr[0] 를 하기 위해 101을 순환
        for j in range(n):
            if i & (1 << j):
                total += arr[j]

        result.add(total)
    return result


def solution1():
    arr.sort()
    subset_sum = subset_sum(arr)

    i = 0
    while True:
        if not i in subset_sum:
            break
        i += 1

    print(i)