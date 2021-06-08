
import cx_Oracle


def dept01_create():
    
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")  # 1.제일 먼저 계정에 커넥트 먼저 실행한다!! 
        try:
            cur = conn.cursor() # 1-1 만약 계정이 일치하여 커넥트가 완성된 경우 바로 커서와 연결한다.
            cur.execute('drop table dept01') # 테이블을 드랍하고
            cur.execute('create table dept01 as select * from dept') # 테이블을 생성한다.
            cur.execute('alter table dept01 add constraint dept01_uk_deptno unique(deptno)') # dept01 테이블의 deptno
        except Exception as e: # 1-2 커서와 연결이 실패하거나 잘못 입력시에 e가 출력되게한다.
            print(e)
        finally: # 예외상황이 발생하더라도 반드시 실행되는 finally 함수
            cur.close()
            conn.close()
    except Exception as e: # 2 커넥트 실패시 e가 출력되도록 한다.
        print(e)


                  # 조건
​​def dept01_query(F_dname): # select 의 역할을 하는 pythonDB 함수 선언 -> dept01에 있는 모든 정보가 출력
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor() # 여기까지는 무조건 해야되는 작용
            cur.execute("select * from dept01 where dname like :dname", dname=F_dname) # select 을 입력 후 셀렉절의있는 조건값을 함수의 변수와 연결 dname = F_dname
            rows = cur.fetchall() # cur.fetchall() 을 사용하여 cur의 있는 모든 내용을 가져옴 
            
            for row in rows:  # fow문을 사용하여 rows 내용을 차례로 print
                print(row)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
    # dept01_insert(10, New York, adress)
def dept01_insert(new_deptno, new_dname, new_loc):  # dept01 테이블에 컬럼의 값을 삽입하기 위해 만든 함수 선언
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("insert into dept01 values(:deptno,:loc :dname,)", deptno=new_deptno, dname=new_dname, loc=new_loc)
            conn.commit() # insert , update 는 commit()을 해줘야한다
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)

                # 바꿀값    #바꿀값   # 조건
def dept01_update(new_dname, new_loc, F_deptno):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("update dept01 set dname=:dname, loc=:loc where deptno=:deptno", dname=new_dname, loc=new_loc, deptno=F_deptno)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)

def dept01_delete(deptno):  # dept01 table에 있는 해당(부서번호)인 컬럼을 삭제
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("delete from dept01 where deptno=:deptno", deptno=deptno)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(e)
        
if __name__ == '__main__':          # 커맨드 : 제일 먼저 실행된다 

    dept01_create()
    dept01_insert(50, 'PD', '강남')
    dept01_query('%ING') # like %S   %S%   S%

    dept01_update(50, 'Playdata','남터')
    dept01_query('%ING')  
​
    dept01_delete(50)
    dept01_query('%ING')
    dept01_query()