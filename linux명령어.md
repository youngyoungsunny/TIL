### 파일 확장자 확인
~~~linux
file 파일명     //UTF-8인지 나옴. (한글이 포함된 파일의 경우, file명령어로 UTF-8인지 확인 필수)
~~~

### 폴더 안 파일 정렬
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
