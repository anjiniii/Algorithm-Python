/*
https://school.programmers.co.kr/learn/courses/30/lessons/181938

문제: 두 수의 연산값 비교하기
날짜: 2025-04-26-토요일

입출력 예 
a	b	result
2	91	364
91	2	912

*/

import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let x = Int("\(a)\(b)")!
    let y = 2 * a * b
    return max(x, y)
}