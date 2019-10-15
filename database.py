from PyQt4 import QtSql,QtGui
import sqlite3

def create_db():
    db = sqlite3.connect("pulp.db")
    
    db.execute("create table if not exists working_days(id int primary key,days varchar(20))")
    db.close()

def insert_into_work(data):
    db = sqlite3.connect("pulp.db")
    for i in data:
        db.execute("insert into working_days values(?,?)",(1,i))
    db.commit()    
    db.close()



create_db()
insert_into_work(["2019-10-01"])
