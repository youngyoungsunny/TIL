### 파일 확장자 확인
~~~
file 파일명     //UTF-8인지 나옴. (한글이 포함된 파일의 경우, file명령어로 UTF-8인지 확인 필수)
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
~~~


### touch : 유효한 bin 파일을 생성하기 위해 씀. 0바이트 파일 생성
~~~linux
 touch 파일명
~~~
옵션 #
-a : 현 시간으로 파일의 접근 시간, 변경 시간을 수정한다.

$ touch -a a
-c : 기존 파일이 없으면 파일이 생성되지 않는다.

$ touch -c abc
abc.txt 라는 파일이 없으면 생성되지 않으며 다음과 같은 메시지가 출력된다.

ls: cannot access abc: no such file or directory
-d : 지정한 시간으로 접근 시간, 수정 시간이 수정되고, 변경시간은 현재 시간으로 수정된다.

$ touch -d '2020-09-22 10:45:30' a
-m : 현 시간으로 파일의 수정 시간, 변경 시간을 수정한다.

$ touch -m a
-r : 지정한 파일의 접근 시간, 수정 시간으로 파일이 수정되고 변경 시간은 현재 시간으로 수정된다.

$ touch -r a b
b 파일의 접근 시간, 수정 시간이 a의 접근 시간, 수정 시간과 동일하게 수정된다.

-t : 지정한 시간으로 접근 시간, 수정 시간을 수정되고 변경 시간은 현재 시간으로 수정된다.

$ touch -t 202009221045.30 a
