/*
https://school.programmers.co.kr/learn/courses/30/lessons/181936

문제: 공배수
날짜: 2025-04-26-토요일

입출력 예 
number	n	m	result
60	    2	3	1
55	    10	5	0

*/

import Foundation

func solution(_ number:Int, _ n:Int, _ m:Int) -> Int {
    if number.isMultiple(of: n) && number.isMultiple(of: m) {
        return 1
    } else {
        return 0
    }
}