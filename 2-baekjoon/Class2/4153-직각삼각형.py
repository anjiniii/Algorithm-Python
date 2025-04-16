"""
2025-04-09-수요일
"""

while True:
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] == arr[2] == 0:
        break

    arr.sort()
    a, b, c = arr[0], arr[1], arr[2]
    if a * a + b * b == c * c:
        print("right")
    else:
        print("wrong")