/*
https://school.programmers.co.kr/learn/courses/30/lessons/181931

문제: 등차수열의 특정한 항만 더하기
날짜: 2025-04-26-토요일

입출력 예 
a	d	included	                                        result
3	4	[true, false, false, true, true]	                37
7	1	[false, false, false, true, false, false, false]	10

*/

import Foundation

// 방법 1 - 나의 풀이
func solution(_ a:Int, _ d:Int, _ included:[Bool]) -> Int {
    var result = 0
    for i in 1...included.count {
        if included[i - 1] {
            result += a + (i - 1) * d
        }
    }
    return result
}

// 방법 2
func solution2(_ a: Int, _ d: Int, _ included: [Bool]) -> Int {
    return included
            .indices                  // 배열의 모든 인덱스 가져오기 [0, 1, 2, ...]
            .filter { included[$0] }  // true만 필터링
            .map { a + d * $0 }       // 등차수열 항 계산
            .reduce(0, +)             // 모든 값 합하기
}