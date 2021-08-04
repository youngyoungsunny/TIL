### 파이썬에서 큐(queue) 자료 구조 : 큐(queue)는 선입선출, FIFO(First In First Out)
- 큐를 사용하면 데이터를 추가한 순서대로 제거할 수 있기 때문에, 스트리밍(streaming), 너비 우선 탐색(breath first search) 등 소프트웨어 개발에서 널리 응용되고 있다. 

- list : 파이썬에서 큐를 사용하는 가장 간단한 방법은 범용 자료 구조인 list 사용하기! 
- list 객체의 pop(0) 함수를 호출하면 첫 번째 데이터를 제거할 수 있다. 

~~~python
>>> queue = [4, 5, 6]
>>> queue.append(7)
>>> queue.append(8)
>>> queue
[4, 5, 6, 7, 8]
>>> queue.pop(0)
4
>>> queue.pop(0)
5
>>> queue
[6, 7, 8]
~~~
- 이런 방식으로 list를 사용하면 뒤에서 **데이터를 추가하고 앞에서 데이터를 제거할 수 있기 때문에** 큐 자료 구조를 사용하는 효과!!!
- 반대 방향으로 큐 자료 구조를 사용하고 싶다면 insert(0, x) 함수를 사용하면 맨 앞에서 데이터를 삽입 가능!  이럴 경우, 데이터가 앞에서 들어가고 뒤로 나오게 됨.

~~~python
>>> queue = [4, 5, 6]
>>> queue.insert(0, 3)
>>> queue.insert(0, 2)
>>> queue
[2, 3, 4, 5, 6]
>>> queue.pop()
6
>>> queue.pop()
5
>>> queue
[2, 3, 4]
~~~
- 하지만 이렇게 list를 큐 자료 구조의 효과를 내기 위해서 사용하는 것은 성능 측면에서 추천되지 않음.
- 파이썬의 list는 다른 언어의 배열처럼 무작위 접근(random access)에 최적화된 자료 구조이기 때문에 pop(0)또는 insert(0, x)는 성능적으로 매우 불리한 연산이다.

- 이 두 연산은 시간 복잡도는 O(N)이기 때문에 담고 있는 데이터의 개수가 많아질 수록 느려짐. 
- 왜냐하면 첫 번째 데이터를 제거한 후에는 그 뒤에 있는 모든 데이터를 앞으로 한 칸식 당겨줘야 하고, 
- 맨 앞에서 데이터를 삽입하려면 그 전에 모든 데이터를 뒤로 한 칸씩 밀어줘야 하기 때문입니다. 
- 이렇게 기존에 queue가 담고 있던 모든 데이터를 앞/뒤로 쉬프트(shift)해주지 않으면 queue[i]의 결과값이 정확하지 않을 것이다. 

-----------------------------------------------------------------------

### deque : collections 모듈의 deque는 double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료 구조!
- deque는 list에는 없는 popleft()라는 메서드를 제공한다.
- 이 메서드를 사용하면 첫 번째 데이터를 제거 가능. 데이터의 흐름은 list 객체의 pop(0) 메서드를 사용할 때 처럼 뒤에서 앞으로 흐르게 됨.

~~~python
>>> from collections import deque
>>>
>>> queue = deque([4, 5, 6])
>>> queue.append(7)
>>> queue.append(8)
>>> queue
deque([4, 5, 6, 7, 8])
>>> queue.popleft()
4
>>> queue.popleft()
5
>>> queue
deque([6, 7, 8])
~~~
- deque는 appendleft(x)라는 메서드도 제공함. 이 메서드를 사용하면 데이터를 맨 앞에서 삽입 가능
- 이 경우, 데이터의 흐름은 list 객체의 insert(0, x) 메서드를 사용할 때 처럼 앞에서 뒤로 흐르게 됩니다.

~~~python
>>> from collections import deque
>>>
>>> queue = deque([4, 5, 6])
>>> queue.appendleft(3)
>>> queue.appendleft(2)
>>> queue
deque([2, 3, 4, 5, 6])
>>> queue.pop()
6
>>> queue.pop()
5
>>> queue
deque([2, 3, 4])
~~~

- **deque의 popleft()와 appendleft(x)메서드는 모두 O(1)의 시간 복잡도를 가지기 때문에, 위에서 살펴본 list의 pop(0)와 insert(0, x) 대비 성능 상에 큰 이점이 있다. **

- 하지만 모든 자료 구조가 그러하듯 deque도 단점이 있다. 
- 바로 무작원 접근(random access)의 시간 복잡도가 O(N)이다. 
- 내부적으로 linked list를 사용하고 있기 때문에 i 번째 데이터에 접근하려면 맨 앞/뒤부터 i 번 순회(iteration)가 필요하기 때문임.

- collections 모듈의 deque에 대한 좀 더 자세한 내용은 아래 파이썬 레퍼런스를 참고하기.

---------------------------------------------------

###파이썬의 우선순위 큐(PriorityQueue) 사용법

collections — Container datatypes — Python 3.8.3 documentation
- Queue : 파이썬에서 큐를 사용하는 마지막 방법은 queue 모듈의 Queue 클래스를 사용한다. 이 방법은 주로 멀티 쓰레딩(threading) 환경에서 사용되며, 내부적으로 라킹(locking)을 지원하여 여러 개의 쓰레드가 동시에 데이터를 추가하거나 삭제할 수 있습니다.
- deque와 달리 방향성이 없기 때문에 데이터 추가와 삭제가 하나의 메서드로 처리된다. 
- 따라서, 데이터가 추가하려면 put(x) 메서드를 사용하고, 데이터를 삭제하려면 get() 메서드를 사용한다.

~~~python
>>> from queue import Queue
>>>
>>> que = Queue()
>>> que.put(4)
>>> que.put(5)
>>> que.put(6)
>>> que.get()
4
>>> que.get()
5
>>> que.get()
6
~~~~

