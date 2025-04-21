"""
2025-04-21
"""


def solution(new_id):
    answer = ''

    # 1단계 소문자로
    new_id = new_id.lower()

    # 2단계 알파벳, 숫자, -_.
    for i in range(len(new_id)):
        char = new_id[i]
        if char.isalpha() or char.isdigit() or char in ["-", "_", "."]:
            answer += char

    new_id = answer
    answer = ""
    # 3단계 연속된 . 하나로 변경
    for i in range(len(new_id)):
        char = new_id[i]
        if char == "." and new_id[i - 1] == ".":
            answer += ""
        else:
            answer += char

    # 4단계 처음과 끝의 . 삭제
    if len(answer) > 0:
        if answer[0] == ".":
            answer = answer[1:]

        if answer[-1] == ".":
            answer = answer[:-1]

    # 5단계 빈문자열은 "a"
    if answer == "":
        answer = "a"

    # 6단계 16글자 이상이면, 15개만 마지막 . 제거
    if len(answer) >= 16:
        answer = answer[:15]
        print(answer[-1])
        while answer[-1] == ".":
            answer = answer[:-1]

    # 7단계 2글자 이하이면, 마지막 문자를 3이 될 때까지 추가
    while len(answer) < 3:
        answer += answer[-1]

    return answer