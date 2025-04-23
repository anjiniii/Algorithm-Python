/*
https://school.programmers.co.kr/learn/courses/30/lessons/181943

문제: 문자열 겹쳐쓰기
날짜: 2025-04-23-수요일

입출력 예 #1
예제 1번의 my_string에서 인덱스 2부터 overwrite_string의 길이만큼에 해당하는 부분은
"11oWor1"이고 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.

*/

import Foundation

func solution(
    _ my_string:String, 
    _ overwrite_string:String, 
    _ s:Int
    ) -> String {
    let endIndex = my_string.index(my_string.startIndex, offsetBy: s)
    let startIndex = my_string.index(my_string.startIndex, offsetBy: s + overwrite_string.count)
    print(my_string[..< endIndex] + overwrite_string + my_string[startIndex ...])

    return ""
}