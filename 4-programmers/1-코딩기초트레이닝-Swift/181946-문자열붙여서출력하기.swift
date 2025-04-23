/*
https://school.programmers.co.kr/learn/courses/30/lessons/181946

문제: 문자열 붙여서 출력하기
날짜: 2025-04-23-수요일

입력 #1
apple pen
출력 #1
applepen

*/


import Foundation

let inp = readLine()!.components(separatedBy: [" "]).map { $0 }
let (s1, s2) = (inp[0], inp[1])

// 방법 1
print("\(s1)\(s2)")

// 방법 2
print(s1 + s2)

// 방법 3
print(inp.joined())