import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="pikobu_db",
    user="postgres",
    password="cccc1835"
)

cursor = connection.cursor()


