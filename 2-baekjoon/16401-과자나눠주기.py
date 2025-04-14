"""
2025-04-14
"""

# m - 조카의 수, n - 막대 과자의 수
m, n = map(int, input().split())
cookies = list(map(int, input().split()))


"""
세 번째 풀이 - 이진탐색 
"""
def check(mid):
    count = 0
    for cookie in cookies:
        count += cookie // mid
        if count >= m:
            return True
    return False


def solution3():
    low, high = 1, max(cookies)
    while low <= high:
        print(low, high)
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid - 1
    print(high)


solution3()


""" 
두 번째 풀이 - 이진 탐색
(1, 과자 막대 최대 길이) 안에서 이진 탐색으로 적절한 길이 찾아감
"""
def solution2():
    start = 1
    end = max(cookies)

    answer = 0
    while start <= end:
        mid = (start + end) // 2

        count = 0
        for cookie in cookies:
            if cookie < mid:
                continue
            else:
                count += cookie // mid

        if count >= m:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)


""" 첫 번째 풀이 - 틀림 """
def solution1():
    if m <= n:
        print(cookies[n - m])
    elif sum(cookies) < m:
        print(0)
    else:
        while len(cookies) < m:
            last = cookies.pop()
            cookies.append(last // 2)
            cookies.append(last - last // 2)
            cookies.sort()
        print(cookies[0])