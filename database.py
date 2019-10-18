from PyQt4 import QtSql,QtGui
import sqlite3

connection = sqlite3.connect("pulp.db")

def create_db():
    db = connection.cursor()
    db.execute("create table if not exists working_days(days varchar(20))")
    #db.execute("create table if not exists machines(id int primary key,")
    db.close()

def insert_into_work(data):
    db = connection.cursor()
    for i in data:
        db.execute("insert into working_days values(?)",[i])
    connection.commit()    
    db.close()

def select_date_from_table(tablename):
    db = connection.cursor()
    res = db.execute("select days from "+tablename)
    return res 
    db.close()


def delete_dates_from_table(data):
    db = connection.cursor()
    db.execute("delete from working_days where days=?",(data,))
    connection.commit()
    db.close()


create_db()
#a=select_date_from_table("working_days")
#insert_into_work(['2019-10-19'])
