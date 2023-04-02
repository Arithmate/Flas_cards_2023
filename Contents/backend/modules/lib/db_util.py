from flask import Flask
import mysql.connector


def __db():
    return mysql.connector.connect(
        host = 'mysql',
        user = 'user',
        passwd = 'iwashi184',
        db = 'cardsdb'
    )

def select(sql):
    connect = __db()
    cursor = connect.cursor(dictionary=True)
    cursor.execute(sql)
    res = []

    for row in cursor.fetchall():
        res.append(row)

    return res

def insert(sql):
    connect = __db()
    cursor = connect.cursor()
    print("#ーーーーーーーーーーーーーーーーー")
    print(sql)
    print("#ーーーーーーーーーーーーーーーーー")
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()

    return None
