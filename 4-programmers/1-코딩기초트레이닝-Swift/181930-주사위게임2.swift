/*
https://school.programmers.co.kr/learn/courses/30/lessons/181930

문제: 주사위 게임 2
날짜: 2025-04-26-토요일

입출력 예 
2	6	1	9
5	3	3	473
4	4	4	110592

*/

import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int) -> Int {
    var result = 0
    if a == b && b == c {
        result += (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c)
    } else if (a == b && b != c) || (a == c && b != c) || (b == b && b != a) {
        result += (a + b + c) * (a * a + b * b + c * c)
    } else if a != b && b != c && a != c {
        result += (a + b + c)
    }
    return result
}

func solution2(_ a: Int, _ b: Int, _ c: Int) -> Int {
    let sum1 = a + b + c
    let sum2 = a * a + b * b + c * c
    let sum3 = a * a * a + b * b * b + c * c * c
    
    if a == b && b == c {
        return sum1 * sum2 * sum3
    } else if a == b || a == c || b == c {
        return sum1 * sum2
    } else {
        return sum1
    }
}

// 다른 사람 풀이
func solution3(_ a:Int, _ b:Int, _ c:Int) -> Int {
    let count = Set([a, b, c]).count
    if count == 3 {
        return a + b + c
    } else if count == 2 {
        return (a + b + c) * (a * a + b * b + c * c)
    } else {
        return (a + b + c) * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c)
    }
}

// GPT
func solution4(_ a: Int, _ b: Int, _ c: Int) -> Int {
    let sum = a + b + c
    let sumSquares = a * a + b * b + c * c
    let sumCubes = a * a * a + b * b * b + c * c * c
    
    switch (a == b, b == c, a == c) {
    case (true, true, true):
        return sum * sumSquares * sumCubes
    case (true, false, false), (false, true, false), (false, false, true):
        return sum * sumSquares
    default:
        return sum
    }
}