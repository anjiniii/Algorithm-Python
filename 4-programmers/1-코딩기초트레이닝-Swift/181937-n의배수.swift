/*
https://school.programmers.co.kr/learn/courses/30/lessons/181937

문제: n의 배수
날짜: 2025-04-26-토요일

입출력 예 
num	n	result
98	2	1
34	3	0

*/

import Foundation

// 방법1 - 나의 풀이
func solution(_ num:Int, _ n:Int) -> Int {
    if num % n == 0 {
        return 1
    } else {
        return 0
    }
}

// 방법2
func solution2(_ num:Int, _ n:Int) -> Int {
    return num.isMultiple(of: n) ? 1 : 0
}