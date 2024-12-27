"""
시각
00시 00분 00초부터 N시 59분 59초까지 3이 하나라도 포함되는 경우의 수
"""

n = int(input())
count = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            clock = str(h) + str(m) + str(s)
            if "3" in clock:
                count += 1

print(count)

"""
풀고나서
아하 이런걸 완전 탐색 Brute Forcing 으로도 분류하는군
데이터 개수가 100만 개 이하일 때 완전 탐색이 적절
"""