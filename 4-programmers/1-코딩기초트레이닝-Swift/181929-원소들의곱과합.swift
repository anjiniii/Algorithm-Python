/*
https://school.programmers.co.kr/learn/courses/30/lessons/181929

문제: 원소들의 곱과 합
날짜: 2025-04-26-토요일

입출력 예 
num_list	     result
[3, 4, 5, 2, 1]	 1
[5, 7, 8, 3]	 0

*/

import Foundation

func solution(_ num_list:[Int]) -> Int {
    let product = num_list.reduce(1, *)
    let sum = num_list.reduce(0, +)
    return product < sum * sum ? 1 : 0
}