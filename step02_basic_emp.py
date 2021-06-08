import cx_Oracle 

# 접속 객체
connection = cx_Oracle.connect(user="SCOTT", password="TIGER",
                               dsn="xe")
print('1---', connection)

# 커서 객체
cursor = connection.cursor()
print('2---', cursor)

# select 한 결과값을 ResultSet 이라 표현
cursor.execute("""select * from dept""")
for deptno, dname, loc in cursor:
    print("Values:", deptno, dname, loc)


cursor.close()
connection.close()