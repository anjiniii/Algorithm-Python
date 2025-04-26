/*
https://school.programmers.co.kr/learn/courses/30/lessons/181934

문제: 조건 문자열
날짜: 2025-04-26-토요일

입출력 예 
ineq	eq	n	m	result
"<"	    "="	20	50	1
">"	    "!"	41	78	0

*/

import Foundation

// 방법 1 - 케이스 2개에 대해 런타임 에러
func solution(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    if ineq == "<" {
        if eq == "=" {
            return n <= m ? 1 : 0
        } else {
            return n < m ? 1 : 0
        }
    } else {
        if eq == "=" {
            return n >= m ? 1 : 0
        } else {
            return n > m ? 1 : 0
        }
    }
}

// 방법 2 - 정답
func solution2(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    if ineq == "<" && eq == "=" {
        return n <= m ? 1 : 0
    } else if ineq == "<" && eq == "!" {
        return n < m ? 1 : 0
    } else if ineq == ">" && eq == "=" {
        return n >= m ? 1 : 0
    } else {
        return n > m ? 1 : 0
    }
}

// 방법 3 - switch 활용
func solution3(_ ineq:String, _ eq:String, _ n:Int, _ m:Int) -> Int {
    switch ineq+eq {
        case ">=": return n >= m ? 1 : 0
        case "<=": return n <= m ? 1 : 0
        case ">!": return n > m ? 1 : 0
        case "<!": return n < m ? 1 : 0
        default: return 0
    }
}