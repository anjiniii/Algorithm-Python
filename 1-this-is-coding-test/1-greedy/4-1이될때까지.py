"""
1이 될 때까지
N이 1이 될 때까지 (N에서 1을 빼기) 또는 (n을 k로 나누기) 를 선택해 반복
나누기는 나누어 떨어질 때만 가능
실행 최소 횟수
"""

n, k = map(int, input().split())

count = 0

while n >= 2:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1
    print(n)

print(count)

"""
(풀고 나서)
1년 전 책에 적어둔 내 풀이와 같았다..!
답안과는 다른데, 놓친 부분이 있는걸까?
"""