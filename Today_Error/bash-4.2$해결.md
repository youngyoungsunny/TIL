~~~console
# 계정을 생성한다.  
root$ groupadd sykim   //- groupadd 명령은 그룹을 추가할때 사용한다. -g : GID를 지정한다. -o : -g 옵션과 함꼐 사용되며 GID를 중복허용한다.
root$ useradd -r -g sykim sykim

# sykim 계정접속
root$ su sykim   //su 명령어는 현재 사용자를 로그아웃하지 않은 상태에서 다른 사용자의 계정으로 전환하는 명령어이다

# 명령어 창이 bash-4.2로 나옴
bash-4.2$
bash-4.2$ exit

# /etc/skel/을 복사한다. 
# rp 옵션을 하면 디렉토리 전체를 묻지도 따지지도 않고 elk디렉토리로 복사한다.
root$ cp -rp /etc/skel/ /home/sykim
root$ chown -R elk.elk /home/sykim

# 다시 접속 한 후에는 bash-4.2$가 나타나지 않음을 확인 가능
root$ su elk
[sykim@****** home]$ 

~~~



#### 혹은 급하게 home에 접근해야한다면?
~~~console
csh     //csh 명령은 C 쉘을 호출, 
      //csh명령어 호출 시, 명령은 사용자의 홈 디렉토리를 조사하여 . cshrc 파일(조정된 사용자 정보를 저장하는 데 사용됨)이 존재하면 해당 파일로부터 명령을 실행하여 시작.
~~~
