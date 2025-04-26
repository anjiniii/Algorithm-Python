/*
https://school.programmers.co.kr/learn/courses/30/lessons/181933

문제: flag에 따라 다른 값 반환하기
날짜: 2025-04-26-토요일

입출력 예 
a	b	flag	result
-4	7	true	3
-4	7	false	-11

*/

import Foundation

func solution(_ a:Int, _ b:Int, _ flag:Bool) -> Int {
    return flag ? a + b : a - b
}