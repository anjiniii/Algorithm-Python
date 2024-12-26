"""
큰 수의 법칙
주어진 수들을 총 M번 더해 가 장 큰 수를 만들기
단, 하나의 값을 K번 까지 더할 수 있음
ex, 2 4 5 4 6 / M = 8 / K = 3
answer, 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46
"""

# n, m, k = map(int, input().split())
n, m, k = 5, 7, 2
nums = [3, 4, 3, 4, 3]

nums.sort(reverse=True)

count = m // (k + 1)
first_count = count * k + m % (k + 1)
second_count = m - first_count

result = nums[0] * first_count + nums[1] * second_count
print(result)

"""
풀고 나서

(처음 풀었던 풀이)
# n, m, k = map(int, input().split())
n, m, k = 5, 8, 3
nums = [2, 4, 5, 4, 6]

nums.sort(reverse=True)

result = nums[0] * k * (m // k) + nums[1] * (m % k)
print(result)

풀이가 더 잘 읽혀야 하는가? 충분히 의도가 잘 전달되었겠지??
가장 큰 수를 K번까지 다 더하고, 그 다음 큰 수를 한 번 더하는 상황에서
가장 큰 수는 m // k 만큼 더해지고, 그 다음 수는 m % k 만큼 더해진다!

틀렸다!!

이 풀이는 해당 테스트 케이스에만 적용될 수 있는 풀이였다

흠 다시 푼 풀이가 주어진 케이스는 맞는데, 정답인지 확실하지 않다..
"""