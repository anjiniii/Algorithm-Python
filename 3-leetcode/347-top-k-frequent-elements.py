"""
2025-03-31-Mon
"""
from collections import Counter


def solution(nums, k):
    counter = Counter(nums)
    most_commons = counter.most_common(k)
    answer = [i[0] for i in most_commons]
    print(answer)


solution(nums=[1, 1, 1, 2, 2, 3], k=2)