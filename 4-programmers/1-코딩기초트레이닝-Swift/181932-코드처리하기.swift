/*
https://school.programmers.co.kr/learn/courses/30/lessons/181932

문제: 코드 처리하기
날짜: 2025-04-26-토요일

입출력 예 
code	        result
"abc1abc1abc"	"acbac"

*/

import Foundation

func solution(_ code:String) -> String {
    let codeArray = Array(code)
    var mode: Int = 0
    var ret: String = ""

    for idx in 0..<code.count {
        if codeArray[idx] == "1" {
            mode = (mode == 1) ? 0 : 1
        } else {
            if mode == 0 && idx.isMultiple(of: 2) {
                ret += String(codeArray[idx])
            } else if mode == 1 && idx.isMultiple(of: 2) == false {
                ret += String(codeArray[idx])
            }
        }
    }

    return ret.isEmpty ? "EMPTY" : ret
}