import mysql.connector

class DB():
    mydb = my_conect = None
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aviva1234!",
            database="sakila"
        )

    def connect(self, sql,q_type):
        connect = self.mydb.cursor()
        connect.execute(sql)
        if q_type == 'select':
            return connect.fetchall()
        else:
            self.mydb.commit()