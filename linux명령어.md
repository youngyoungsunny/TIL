### 파일 확장자 확인
~~~console
file 파일명  //출력결과: UTF-8  

(한글이 포함된 파일의 경우, file명령어로 UTF-8인지 확인 필수)    
~~~

### 폴더 안 파일 정렬 (ls = list segments)
~~~console
ls  //list segments의 약자, 파일과 directory 정보 제공
ls -ltr
ls -altr

ls -l
~~~

### diff 비교 명령어
~~~console
sdiff  file1  file2        //프로그램 수정 후, 파일 변경 전 후 비교
~~~

### 정렬 명령어
~~~console
sort bbb

sort -u bbb   // -u : 중복제거
~~~


### find : 파일 찾기
~~~console
find . -name 'sykim'
~~~


### grep : 파일에서 내가 원하는 keyword를 찾아줌
~~~console
grep 'sykim' /etc/passwd
grep B1XX.AXX* B2XX.AXX* | "14:" | wc   // wc 명령어란? wc : 주어지는 파일 또는 표준 입력의 바이트, 문자, 단어 그리고 줄(라인) 수를 출력해주는 명령어입니다. wc 는 'word count'를 의미

grep 'KEYWORD' *.sql    //해당 dir에 있는 .sql로 끝나는 파일에서 'KEYWORD'를 찾는다.
~~~


<br/><br/><br/><br/>
### touch : 유효한 bin 파일을 생성하기 위해 씀. 0바이트 파일 생성
~~~console
touch [파일명]
~~~
## touch 옵션 #
- a : 현 시간으로 파일의 접근 시간, 변경 시간을 수정
~~~console 
touch -a a
~~~

- c: 기존 파일이 없으면 파일이 생성되지 않는다.
~~~consloe
touch -c abc
~~~
이 경우, abc.txt 라는 파일이 없으면 생성되지 않으며 다음과 같은 메시지가 출력된다.
~~~
ls: cannot access abc: no such file or directory
~~~


- d : 지정한 시간으로 접근 시간, 수정 시간이 수정되고, 변경시간은 현재 시간으로 수정
~~~consloe
touch -d '2020-09-22 10:45:30' a
~~~


- m : 현 시간으로 파일의 수정 시간, 변경 시간을 수정
~~~consloe
touch -m a
~~~~
<br/><br/><br/><br/>

### cat 명령어 
~~~consloe
cat file1    //file1 파일을 연다.

cat -b file1  //각 행에 번호를 붙여서 출력

cat -n file1  //빈 행에도 번호를 붙여서 출력

cat -s file1  //연속되는 2개 이상의 빈행을 하나의 행으로 출력
~~~


### head : 파일의 앞 부분부터 확인하는 명령어 
~~~consloe
head file1   //file1의 10행까지만 출력(default)

head -n 20 file1  //file1의 20줄까지 출력

head -c 200 file1  //file1의 200byte까지의 내용을 출력
~~~


### tail : 파일의 마지막 부분을 확인하는 명령어
- 실무에서는 특정 파일에 계속 추가되는 모든 내용을 모니터링 할 수 있어서 유용.
- /log dir에 존재하는 많은 시스템로그파일들의 로그 내용을 실시간으로 모니터링하기 위한 용도로 많이 쓰임.
~~~consloe
tail file1   //file1의 마지막 10개행을 출력

tail -n 20 file1  //file1의 마지막 부분의 20개행까지 출력

tail -c 200 file1  //file1의 마지막에서 200byte까지를 출력


#### 로그파일을 실시간으로 모니터링
tail -f /var/log/messages    //종료는 ctrl+c

~~~


### pwd : 현재 dir 확인
~~~console

pwd

>>/home/testdir

~~~


### clear : cmd 창에 보이는 내용을 모두 clear함

###
### vim 명령어

> 잠깐! vi vs vim는 무슨 차이인가요?
>> UNIX의 기본 편집기가 vi, vi를 개량한 버전이 vim 에디터
>> VIM : Vi IMproved (향상된 Vi)
|
