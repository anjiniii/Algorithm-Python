/*
https://school.programmers.co.kr/learn/courses/30/lessons/181949

문제: 대소문자 바꿔서 출력하기
날짜: 2025-04-21-월요일

입력 #1
aBcDeFg
출력 #1
AbCdEfG

*/

import Foundation

let s1 = readLine()!

var answer = ""
for s in s1 {
    if s.isUppercase {
        answer.append(s.lowercased())
    } else {
        answer.append(s.uppercased())
    }
}

print(answer)
