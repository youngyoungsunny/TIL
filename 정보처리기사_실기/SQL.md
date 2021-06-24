### 순서  
select<br/>
from <br/>
where <br/>
group by having  <br/> 
order by ASC | DESC<br/><br/><br/><br/>

### DDL


### DDL
- insert<br/>
- delete<br/>

### DCL
grant<br/>
revoke<br/>

### TCL (트랜잭션 제어)
commit <br/>
rollback <br/>
check point (롤백을 위한 시점 설정) <br/><br/><br/>


~~~sql
select *   
from student
where dept = '컴퓨터과학';
~~~~


~~~sql
select *
from 학생
where 학년 =1 or 수강과목 = '운영체제';  //and
~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~


~~~sql

~~~

-----------------------------------------------
## 기출분석
### 2020년 정보처리기사 실기 SQL 작성 문제 분석
 
- 2020년 1회차 SQL 문제 (1문제) <br/>
1.  SQL DML - 실행 결과 작성<br/>

학생(STUDENT) 테이블에 컴퓨터정보과 학생 50명, 인터넷정보과 학생 100명, 사무자동화과 학생 50명에 관한 데이터가 있다고 했을 때, <br/>
다음에 주어지는 SQL문 (1), (2), (3)을 각각 실행시키면, 결과 튜플 수는 각각 몇 개인가? (단, DEPT는 학과 컬럼명임) <br/><br/><br/>

(1) SELECT DEPT FROM STUDENT;
(2) SELECT DISTINCT DEPT FROM STUDENT;
(3) SELECT COUNT (DISTINCT DEPT) FROM STUDENT WHERE DEPT='컴퓨터정보과';

정답 : (1) 200   (2) 3    (3) 1

-----------------------------------------
## - 2020년 2회차 SQL 문제 (2문제)

1. SQL DML (in 사용) - 학번, 이름을 학생 테이블에서 3, 4학년인 학생을 검색하는 명령어 작성

~~~sql
 select 학번, 이름
 from 학생
 where 학년 in (3,4);
~~~

2. SQL DDL 인덱스 작성 - student 테이블의 name 속성에 idx_name 이름의 인덱스를 생성하는 명령어 작성

~~~sql
create INDEX idx_name
ON student(name);
~~~

--------------------------------------------------------------------
## - 2020년 3회차 SQL 문제 (3문제)
1. SQL DDL 테이블에 속성 추가 - 빈칸 채우기 <br/>

( ① ) TABLE 학생 ( ② ) 주소 VARCHAR(20); <br/>

정답: ① ALTER ② ADD <br/>


2. SQL DML - 성적 테이블에서 과목별 점수의 평균이 90이상인 과목이름 최소점수 최대점수 출력하는 명령어 작성 <br/>

- WHERE 구문 사용 X, GROUP BY, HAVING, AS 사용 <br/>

~~~sql
select 과목이름, MIN(점수) as 최소점수, MAX(점수) as 최대점수
from 성적
where 
~~~



3. SQL DML - 학생 테이블에서 이름이 민수인 튜플 삭제하는 명령문 작성

~~~sql
DELETE FROME 학생 WHERE 이름 = '민수';
~~~

<br/><br/><br/>
 
----------------------------------------
## - 2020년 4, 5회차 SQL 문제 (1문제)

1. SQL DML - 학생 테이블에서 학과와 학과별 튜플 수를 출력하는 명령문 작성

- where 쓰지말 것, group by 쓸 것, 집계함수 사용할 것, AS(alias)사용할 것, 세미콜론(;) 생략 가능, 인용 필요시 ' 사용 

- 결과 테이블:

| 학과	| 학과별튜플수|
| 전기	| 1 |
| 컴퓨터 |	2 |
| 전자	| 2 |

~~~sql
select 학과, count(학과) as '학과별튜플수'
from 학생
group by 학과;
~~~

~~~sql
select 학과, count(*) as '학과별튜플수'
from 학생
group by 학과;
~~~
