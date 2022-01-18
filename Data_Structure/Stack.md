Stack : 쌓는 자료형, 책을 쌓는 것을 생각하면 매우 쉽다. 선형으로 나열된 자료구조이다 <br/>

### Stack의 연산
- push : 맨 위에 원소 추가
- pop : 맨 위의 원소를 제거
- peek() : 스택 가장 위에 있는 원소 반환 (삭제는 X)
- empty() 스택이 비어있다면 1, 아니면 0을 반환



### 파이썬에서는?
- 파이썬에서는 stack을 list 또는 linked list로 구현한다.
- Stack.append() : 리스트 맨 끝에 원소를 추가, 시간복잡도 : O(1)
- Stack.pop(i) : 리스트의 i번째 원소를 삭제,
- Stack.pop(-1) : 맨 앞에 있는 원소를 삭제, 시간복잡도: O(1)



### 파이썬에서 stack 사용
~~~python
from collections import deque

dq=deque() # 덱 생성
dq.append() # 덱의 가장 오른쪽에 원소 삽입
dq.popleft() # 가장 왼쪽 원소 반환
dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
dp.pop() # 가장 오른쪽 원소 반환
dp.clear() # 모든 원소 제거
dp.copy() # 덱 복사
dp.count(x) #x와 같은 원소의 개수를 계산
~~~

