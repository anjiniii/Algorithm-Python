/*
https://school.programmers.co.kr/learn/courses/30/lessons/181944

문제: 홀짝 구분하기
날짜: 2025-04-23-수요일

입력 #1
100
출력 #1
100 is even

*/

import Foundation

let a = Int(readLine()!)!

// 방법 1
if a.isMultiple(of: 2) {
    print("\(a) is even")
} else {
    print("\(a) is odd")
}

// 방법 2
print("\(a) is \(a.isMultiple(of: 2) ? "even" : "odd")")