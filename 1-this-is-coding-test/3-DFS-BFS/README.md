## DFS/BFS

### 자료구조
데이터를 표현하고 관리하고 처리하기 위한 구조

- 삽입: push, 데이터를 삽입
- 삭제: pop, 데이터를 삭제


- 오버플로: 이미 가득 찬 상태에서 삽입
- 언더플로: 전혀 들어 있지 않은 상태에서 삭제


### 스택
First In Last Out || Last In First Out

선입후출, 후입선출

파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요 없음<br>
기본 리스트에서 append(), pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작
```python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최하단 원소부터 출력
print(stack)
# 최상단 원소부터 출력
print(stack[::-1])
```

```python
# 출력결과
[5, 2, 3, 1]
[1, 3, 2, 5]
```


### 큐
