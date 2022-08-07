### 관계 데이터 연산
- 관계대수(Relational Algebra) : 릴레이션에서 사용자가 원하는 결과를 얻기 위해 연산자를 표현하는 방법으로 결과를 얻기 위한 절차를 표현하기 때문에 "절차적언어"라고 한다.
- 순수 관계 연산자 : select, project, join, division
- 일반 집합 연산자 : 합집합, 교집합, 차집합, 카티젼 프로덕트

-관계해석 : 릴레이션에서 결과를 얻기 위한 과정을 표현한 것으로 연산자 없이 정의하는 방법을 이용하는 "비절차적" 언어이다.

### SQL문 순서
~~~sql
select
from 
where
group by having  
order by ASC | DESC
~~~
------------------------------------------------------
#### DDL : create, alter, drop
#### DML : select, insert, update, delete
#### DCL : commit(연산이 성공적으로 종료되어 연산에 의한 수정내용을 지속적으로 유지하기 위한 명령어), 
   rollback(비정상적인 종료 혹은 정상적 수행이더라도 그 전으로 돌리기 위해서 연산내용을 취소)
------------------------------------------------------
### DDL
- insert<br/>
- delete<br/>

### DCL
- grant<br/>
- revoke<br/>

### TCL (트랜잭션 제어)
- commit <br/>
- rollback <br/>
- check point (롤백을 위한 시점 설정) <br/><br/><br/>  
-------------------------------------------------------

~~~sql
select *   
from student
where dept = '컴퓨터과학';
~~~~


~~~sql
select *
from 학생
where 학년=1 or 수강과목='운영체제';  //and
~~~


~~~sql
select distinct 수강과목   //distinct : 중복값 제거
from 학생
where 학생 >= 2;
~~~


~~~sql

집계함수 : sum() , avg(), max(), min(), count()


select sum(점수)
from 학생
where 학년 = 1;

~~~


~~~sql
//order by

select 성명
from 학생
where 점수 >= 85
order by 학번 ASC;  //DESC

~~~


~~~sql
select 학년
from 학생
group by 학년
having count(*)>=2 ;

//학생 테이블에서 2명 이상인 학년을 검색하시오.
~~~


~~~sql
//부속(하위)질문

select 학생수
from 학과 인원
where = 학과 = 
 (select 학과
  from 학생정보
  where 이름 = '이영진');
~~~


~~~sql
//부분 매치 질의문
select 성명
from 학생
where 연락처 like '%7588';
~~~


~~~sql
insert into 테이블이름(학번, 성명, 학년, 수강과목, 연락처) values (051115, '김정미', 4, '데이터베이스', '243-0007');
~~~


~~~sql
// 학생 테이블에서 '이영진' 학생의 저수를 92점으로 수정하시오.
update 학생
set 점수 = 92
where 성명 = '이영진';
~~~


~~~sql
delete from 학생
where 학년 = 2 ;
~~~


~~~sql

delete from 학생; //학생 테이블 전체 삭제
~~~

~~~sql
//뷰의 생성

create view 3학년연락처(학번, 이름, 전화번호)
as select 학번, 성명 연락처
from 학생
where 학년 = 3 ; 
~~~~


~~~sql

drop view 학생 restrict | cascade ; 


~~~

-----------------------------------------------------------
#### 단일행 서브쿼리
~~~ sql
select *
from 성적
where 학과 = (select 학과 from 성적 where 성명 = '김영진');
~~~
- 단일행의 경우,  =, > , < , <= , >=  을 쓴다.


### 다중행 서브쿼리
~~~ sql
select *
from 성적
where 점수 > ( select 점수 from 성적 where 성명 = '강희영');
~~~

- 다중행인 경우, in, any, some, all, exists 키워드를 쓴다.


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
