from flask import Flask
import mysql.connector


def __db():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'user',
        passwd = 'iwashi184',
        db = 'cardsdb'
    )

def select(sql):
    connect = __db()
    cursor = connect.cursor()
    cursor.execute(sql)
    res = []

    for row in cursor.fetchall():
        res.append(row)

    return res

def insert(sql):
    connect = __db()
    cursor = connect.cursor()
    cursor.execute(sql)

    return None
