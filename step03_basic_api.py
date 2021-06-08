# step03_basic_api.py
import cx_Oracle 

connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
print("Database version:", connection.version)

cur = connection.cursor()

# https://cx-oracle.readthedocs.io/en/latest/user_guide/sql_execution.html#fetch-methods
# for row in cur.execute("""select * from dept"""):
#     print(row, type(row))   # tuple  타입
#     print(row[0])   # tuple 객체의 첫번째 요소 데이터 출력
    

cur.execute("select * from dept")


# while True:
#     row = cur.fetchone()  # 한 row씩 반환하는 함수 
#     if row is None:
#         break
#     print(row)

# num_rows = 5  
# while True:
#     rows = cur.fetchmany(num_rows)   # resultset에서 한번에 반환 받고자 하는 row수
#     print(1)
#     if not rows:
#         break
#     for row in rows:
#         print(row)


# 검색된 resultset 정보를 보유한 cursor로 부터 모든 resultset을 반환
rows = cur.fetchall()
for row in rows:
    print(row)


# 자원 반환 순서 중요
cur.close()
connection.close()


