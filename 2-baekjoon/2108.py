# 2108
# 통계학
# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

n = int(input())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]

data.sort()

# 산술 평균
print(round(sum(data) / n))

# 중앙값
# print(data[int(n/2)])
print(data[n // 2])

# 최빈값
counter = Counter(data)
max_frequency = max(counter.values())
most_frequent_values = [key for key, count in counter.items() if count == max_frequency]
most_frequent_values.sort()
if len(most_frequent_values) == 1:
    print(most_frequent_values[0])
else:
    print(most_frequent_values[1])

# 범위
print(data[-1] - data[0])


"""
풀고나서
정수의 절댓값이 4000을 넘지 않으니
-4000 ~ 4000 의 8001개의 공간을 만들고 진행해도 될 것 같다는 생각이 든다.. 흠 
"""