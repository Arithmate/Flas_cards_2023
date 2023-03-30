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
    print("dbbbbbbbbbbbbbbb")

    for row in cursor.fetchall():
        print("###", row)
        res.append(row)

    return res

def insert(sql):
    connect = __db()
    cursor = connect.cursor()
    cursor.execute(sql)

    return None
