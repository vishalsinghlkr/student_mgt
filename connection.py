import psycopg2
def connection():
    return psycopg2.connect(
        host="localhost",
        database="test_db",
        user="postgres",
        password="vishal@11",
        port="5433"
    )
conna = connection()