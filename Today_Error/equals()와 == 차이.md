### equals()

String s라는 변수에 값을 할당했지만, 만약 값이 할당되지 않는다면 

변수.equal() 부분 즉, s.equals("변수") 부분에서 nullexception이 발생하기 때문이죠.

 

그럼 어떻게 방지할 수 있을까요? 사실 null check 로직을 넣으면 됩니다.

if(s != null) 을 심어서 체크하면 되지요.
