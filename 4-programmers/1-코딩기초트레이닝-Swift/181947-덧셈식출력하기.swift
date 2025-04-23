/*
https://school.programmers.co.kr/learn/courses/30/lessons/181947

문제: 덧셈식 출력하기
날짜: 2025-04-23-수요일

입력 #1
4 5
출력 #1
4 + 5 = 9

*/

import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])

print("\(a) + \(b) = \(a + b)")