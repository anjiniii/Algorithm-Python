/*
https://school.programmers.co.kr/learn/courses/30/lessons/181950

문제: 문자열 반복해서 출력하기
날짜: 2025-04-21-월요일

입력 #1
string 5
출력 #1
stringstringstringstringstring

*/

import Foundation

let inp = readLine()!.components(separatedBy: [" "]).map { $0 }
let (s1, a) = (inp[0], Int(inp[1])!)

print(String(repeating: s1, count: a))