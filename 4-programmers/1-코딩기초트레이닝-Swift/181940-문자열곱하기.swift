/*
https://school.programmers.co.kr/learn/courses/30/lessons/181940

문제: 문자열 곱하기
날짜: 2025-04-26-토요일

입출력 예 
my_string	k	result
"string"	3	"stringstringstring"
"love"	    10	"lovelovelovelovelovelovelovelovelovelove"
*/

import Foundation

func solution(_ my_string:String, _ k:Int) -> String {
    return String(repeating: my_string, count: k)
}