import psycopg2

# PostgreSQL 연결 정보
conn = {
    'port': '5432',
    'user': 'postgres',
    'password': '1234',
}

# PostgreSQL 연결
connection = psycopg2.connect(**conn)

# 커서 생성
cursor = connection.cursor()

# account 테이블에서 모든 정보를 선택
cursor.execute('SELECT * FROM application.account')

# 결과 가져오기
result = cursor.fetchall()

# 결과 출력
for row in result:
    print(row)

# 연결 및 커서 닫기
cursor.close()
connection.close()