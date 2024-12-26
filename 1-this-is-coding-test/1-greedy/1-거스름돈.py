"""
예제 3-1 거스름돈
500원, 100원, 50원, 10원 무한히 존재
손님에게 거슬러 줘야 할 금액 N원 (N은 항상 10의 배수)
거슬러 줘야 할 동전의 최소 개수
"""

n = 3270    # 거스름돈
coins = [500, 100, 50, 10]  # 동전의 종류
count = 0   # 동전의 개수
remain = n  # 나머지

for coin in coins:
    count += remain // coin
    remain = remain % coin

print("정답: " + str(count))

"""
풀고 나서
remain 없이 n으로 사용 해도 될 것 같다!!
"""