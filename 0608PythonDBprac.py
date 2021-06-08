# oracle driver 모듈 사용 선언

import cx_Oracle

def dept01_create():
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()
    except:
        print('아이디와 패스워드를 제대로 입력하세요!!')
    finally:
        print('예외 발생과 무관하게 실행되는 영역 자원반환')
        
                               




        try:
            cur.execute('drop table dept01')
            cur.execute('create table dept01 as select deptno, dname from dept')
        except:
            print('드랍할 테이블이 없거나 이미 만들어져 있습니다.')
        finally:
            print('예외 발생과 무관하게 실행되는 영역 자원반환')
            cur.close()
            conn.close()


def dept01_query():
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER",
                               dsn="xe")
    except:
        print('아이디와 패스워드를 제대로 입력하세요!!')
    finally:
        print('예외 발생과 무관하게 실행되는 영역 자원반환')
        cur.close()
        conn.close()

        cur = conn.cursor()

        try:
            cur.execute('select * from dept01')
            rows = cur.fetchall()

            for row in rows:
                print(row)
        except:
            print('잘못입력하였거나 찾을 테이블이 없습니다.')
        finally:
            print('예외 발생과 무관하게 실행되는 영역 자원반환')
            cur.close()
            conn.close() 

def dept01_query_one(deptno):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER",
                               dsn="xe")
        cur = conn.cursor()
    except:
        print('아이디와 패스워드를 제대로 입력하세요!!')
    finally:
        print('예외 발생과 무관하게 실행되는 영역 자원반환')
        cur.close()
        conn.close() 

        
        try:
            cur.execute('select * from dept01 where deptno=:deptno', deptno = deptno)

            # 결과가 하나의 row
            row = cur.fetchone()
            print(row)
        except:
            print('잘못입력하였거나 찾을 테이블이 없습니다')
        finally:
            print('예외 발생과 무관하게 실행되는 영역 자원반환')
            cur.close()
            conn.close()

def dept01_insert(new_deptno, new_dname):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER",
                               dsn="xe")
        cur = conn.cursor()
    except:
        print('아이디와 패스워드를 제대로 입력하세요!!')
    finally:
        print('예외 발생과 무관하게 실행되는 영역 자원반환')
        cur.close()
        conn.close()
        try:    
            cur.execute("insert into dept01 values(:new_deptno, :new_dname)",new_deptno=new_deptno, new_dname=new_dname)
        
            conn.commit()
        except:
            print('잘못입력하였거나 테이블이 존재하지않습니다')
        finally:
            print('예외 발생과 무관하게 실행되는 영역 자원반환')
            cur.close()
            conn.close()



def dept01_update(deptno, new_dname):

    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER",
                               dsn="xe")
        cur = conn.cursor()
    except:
        print('아이디와 패스워드를 제대로 입력하세요!!')
    finally:
        print('예외 발생과 무관하게 실행되는 영역 자원반환')
        cur.close()
        conn.close()

        try:    
            cur.execute('update dept01 set dname=:new_dname where deptno=:deptno', new_dname=new_dname, deptno=deptno)

            conn.commit()
        except:
            print('잘못입력하였거나 테이블이 존재하지않습니다')
        finally:
            print('예외 발생과 무관하게 실행되는 영역 자원반환')
            cur.close()
            conn.close()


def dept01_delete(deptno):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER",
                                dsn="xe")
        cur = conn.cursor()
        conn.commit()
    except:
        print('잘못입력하였거나 테이블이 존재하지않습니다')

    finally:
        cur.close()
        conn.close()

        try:        
            cur.execute('delete from dept01 where deptno=:deptno',deptno=deptno)
        except:
            print('잘못입력하였거나 테이블이 존재하지않습니다')
        finally:
            cur.close()
            conn.close()

if __name__ == '__main__':
    