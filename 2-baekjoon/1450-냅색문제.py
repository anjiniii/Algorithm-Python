"""
2025-04-02-수요일
2025-04-03-목요일

n개의 물건, c만큼의 무게 가능
"""

from bisect import bisect_right


def subset_sum(arr):
    result = []
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

        result.append(total)
    return result


n, c = map(int, input().split())
weights = list(map(int, input().split()))

left = weights[: n // 2]   # 왼쪽 반
right = weights[n // 2 :]  # 오른쪽 반

sum_left = subset_sum(left)    # 왼쪽 배열의 부분집합 합 리스트
sum_right = subset_sum(right)  # 오른쪽 배열의 부분집합 합 리스트

sum_right.sort()

print(sum_left)
print(sum_right)

count = 0
# (x + y ≤ C)인 모든 조합의 수 구하기
for x in sum_left:
    # x + y <= c → y <= c - x
    # 왼쪽 합 + 오른쪽 합 <= c 를 만족하려면 오른쪽 합 <= c - 왼쪽 합
    # bisect_right(a, b)는 a에서 b 이하인 값이 몇 개인지
    count += bisect_right(sum_right, c - x)

print(count)