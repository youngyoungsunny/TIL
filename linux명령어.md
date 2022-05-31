### 파일 확장자 확인
~~~
file 파일명  //출력결과: UTF-8  

(한글이 포함된 파일의 경우, file명령어로 UTF-8인지 확인 필수)    
~~~

### 폴더 안 파일 정렬 (ls = list segments)
~~~linux
ls  //list segments의 약자, 파일과 directory 정보 제공
ls -ltr
ls -altr

ls -l
~~~

### diff 비교 명령어
~~~linux
sdiff  file1  file2        //프로그램 수정 후, 파일 변경 전 후 비교
~~~

### 정렬 명령어
~~~linux
sort bbb

sort -u bbb   // -u : 중복제거
~~~


### find : 파일 찾기
~~~linux
find . -name 'sykim'
~~~


### grep : 파일에서 내가 원하는 keyword를 찾아줌
~~~linux
grep 'sykim' /etc/passwd
grep B1XX.AXX* B2XX.AXX* | "14:" | wc   // wc 명령어란? wc : 주어지는 파일 또는 표준 입력의 바이트, 문자, 단어 그리고 줄(라인) 수를 출력해주는 명령어입니다. wc 는 'word count'를 의미
~~~
<br/><br/><br/><br/>
### touch : 유효한 bin 파일을 생성하기 위해 씀. 0바이트 파일 생성
~~~linux
 touch [파일명]
~~~
#### touch 옵션 #
- a : 현 시간으로 파일의 접근 시간, 변경 시간을 수정
~~~linux
$ touch -a a
~~~

- c: 기존 파일이 없으면 파일이 생성되지 않는다.
~~~
$ touch -c abc
~~~
이 경우, abc.txt 라는 파일이 없으면 생성되지 않으며 다음과 같은 메시지가 출력된다.
~~~
ls: cannot access abc: no such file or directory
~~~


- d : 지정한 시간으로 접근 시간, 수정 시간이 수정되고, 변경시간은 현재 시간으로 수정
~~~
$ touch -d '2020-09-22 10:45:30' a
~~~


- m : 현 시간으로 파일의 수정 시간, 변경 시간을 수정
~~~
$ touch -m a
~~~~
<br/><br/><br/><br/>


### vim 명령어

> 잠깐! vi vs vim는 무슨 차이인가요?
>> UNIX의 기본 편집기가 vi, vi를 개량한 버전이 vim 에디터
>> VIM : Vi IMproved (향상된 Vi)
|
