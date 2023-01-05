import math
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="pikobu_db",
    user="postgres",
    password="cccc1835"
)

cursor = connection.cursor()
def passwordHash(rawPass:str):
    passSum = 0
    for letter in rawPass:
        passSum += ord(letter)
    return int(math.sin(passSum) * 10**16)

# print(passwordHash('qwerty'))

def registration():
    while True:
        login = input('Please input your username:')
        query = "SELECT user_login FROM users_table WHERE user_login='" + login + "'"
        cursor.execute(query)
        if cursor.fetchall():
            print('This username is already taken. Try again')
        else:
            break
    password = passwordHash(input('Please input your password:'))
    query = "INSERT INTO users_table(user_login, user_password)" \
            "VALUES('" + login + "','" + str(password) + "')"
    cursor.execute(query)
    connection.commit()

def logIn():
    global thisUserId
    while True:
        login = input('Please input your username:')
        password = passwordHash(input('Please input your password:'))
        query = "SELECT user_id FROM users_table WHERE user_login='" + login + "' AND user_password='" + str(password) + "'"
        cursor.execute(query)
        thisId = cursor.fetchall()
        if thisId:
            print('You are logged in!')
            thisUserId = thisId[0][0]
            print(thisUserId)
            return
        else:
            print('Username or Password is not correct. Try again!')

# registration()
logIn()