/*
https://school.programmers.co.kr/learn/courses/30/lessons/181935

문제: 홀짝에 따라 다른 값 반환하기
날짜: 2025-04-26-토요일

입출력 예 
n	result
7	16
10	220

*/

import Foundation

// 방법 1 - 나의 풀이
func solution(_ n:Int) -> Int {
    if n.isMultiple(of: 2) {
        var answer = 0
        for i in 1...(n / 2) {
            answer += (2 * i) * (2 * i)
        }
        return answer
    } else {
        return (n + 1) * (n + 1) / 4
    }
}

// 방법 2
func solution2(_ n:Int) -> Int {
    if n % 2 == 0 {
        return stride(from: 2, through: n, by: 2).reduce(0) { $0 + $1 * $1 } 
    } else { 
        return stride(from: 1, through: n, by: 2).reduce(0, +) 
    }
}