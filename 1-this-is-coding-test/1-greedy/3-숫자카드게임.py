"""
숫자 카드 게임
N X M 숫자 카드가 놓여져 있고
행 선택 후, 가장 작은 숫자를 선택하게 된다
선택될 수 있는 값 중 가장 큰 수는?
"""

n, m = map(int, input().split())

max_num = 0
for n in range(1, n + 1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    if max_num < numbers[0]:
        max_num = numbers[0]

print(max_num)

# 책 답안 1
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)