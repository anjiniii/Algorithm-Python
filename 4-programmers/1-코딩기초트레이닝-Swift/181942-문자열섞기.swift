/*
https://school.programmers.co.kr/learn/courses/30/lessons/181942

문제: 문자열 섞기
날짜: 2025-04-26-토요일

입출력 예 #1
str1	str2	result
"aaaaa"	"bbbbb"	"ababababab"

*/

import Foundation

// 방법 1 - 나의 첫 번째 풀이
func solution(_ str1:String, _ str2:String) -> String {
    let str1Array = Array(str1)
    let str2Array = Array(str2)
    var answer = ""
    for i in (0...(str1.count - 1)) {
        answer += String(str1Array[i])
        answer += String(str2Array[i])
    }
    return answer
}

// 방법 2 - zip 활용
func solution2(_ str1:String, _ str2:String) -> String {
    var result: String = ""
    for (one, two) in zip(str1, str2) {
        result.append(one)
        result.append(two)
    }
    return result
}

// 방법 3 - zip 활용
func solution(_ str1:String, _ str2:String) -> String {
    return zip(str1, str2).map { String($0) + String($1) }.joined()
}

print(solution2("aaaaa", "bbbbb"))