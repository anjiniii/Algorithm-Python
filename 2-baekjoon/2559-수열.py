"""
2025-04-04-금요일
슬라이딩 윈도우
"""


def solution(n, k, arr):
    if n == k:
        return sum(arr)

    max_total = sum(arr[:k])
    total = sum(arr[:k])
    for i in range(k, n):
        total = total + arr[i] - arr[i - k]
        max_total = max(max_total, total)

    return max_total


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(n, k, arr))