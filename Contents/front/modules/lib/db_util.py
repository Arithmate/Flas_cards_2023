from flask import Flask
import mysql.connector

class DataBase:

    def __init__(self):
        self.connect = mysql.connector.connect(
            host = 'mysql',
            user = 'user',
            passwd = 'iwashi184',
            db = 'cardsdb'
        )
        self.cursor = self.connect.cursor(dictionary=True)

    def select(self, sql):
        self.cursor.execute(sql)
        res = []
        for row in self.cursor.fetchall():
            res.append(row)
        return res

    def insert(self, sql):
        self.cursor.execute(sql)
        return None

    def commit(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
        return None
