/*
https://school.programmers.co.kr/learn/courses/30/lessons/181928

문제: 이어 붙인 수
날짜: 2025-04-26-토요일

입출력 예 
num_list	     result
[3, 4, 5, 2, 1]  393
[5, 7, 8, 3]	 581

*/

import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd: String = ""
    var even: String = ""
    num_list.forEach { i in
        if i.isMultiple(of: 2) {
            even += String(i)
        } else {
            odd += String(i)
        }
    }
    return Int(odd)! + Int(even)!
}