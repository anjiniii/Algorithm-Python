/*
https://school.programmers.co.kr/learn/courses/30/lessons/181939

문제: 더 크게 합치기
날짜: 2025-04-26-토요일

입출력 예 
a	b	result
9	91	991
89	8	898

*/

import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let x = Int(String(a) + String(b))!
    let y = Int(String(b) + String(a))!
    return max(x, y)
}