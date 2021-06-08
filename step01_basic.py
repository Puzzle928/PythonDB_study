import cx_Oracle # oracle db를 쉽게 활용 가능하게 해주는 driver


# connect(): id/pw/dsn 값으로 db 접속



connection = cx_Oracle.connect(user="hr", password="hr",
                               dsn="xe")
print('db 접속 성공')

cursor = connection.cursor()
# execute() : query(select, 질의) 문장 실행 가능한 함수
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = 50,
        eid = 190)
for fname, lname in cursor:
    print("Values:", fname, lname)


# 자원 반환 필수
cursor.close()
connection.close()