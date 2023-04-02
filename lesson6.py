# база_данных
# sql - язык структурированных данных
# СУБД-системы управления баз данных (можно называть фреймворк или библиотека)
# реляционные(Реляционная база данных – это набор данных с предопределенными связями между ними. Эти данные организованны в виде набора таблиц, состоящих из столбцов и строк. В таблицах хранится информация об объектах, представленных в базе данных), нереалиационные(Нереляционная база данных — это база данных, в которой в отличие от большинства традиционных систем баз данных не используется табличная схема строк и столбцов. В этих базах данных применяется модель хранения, оптимизированная под конкретные требования типа хранимых данных.)
# CRUD CREATE(добавление) REED(чтение) UPDATE(изменение) DELETE

import sqlite3
from sqlite3 import Error


def create_connektion(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def reed(conn):
    try:
        sql='SELECT * FROM student'
        cursor = conn.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()

        for i in rows:
            print(i)
    except Error as e:
        print(e)




def create_student(conn, student):
    sql = '''INSERT INTO student (name,mark,hobby,b_date,is_married)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor=conn.cursor()
        cursor.execute(sql,student)
        conn.commit()
    except Error as e:
        print(e)
#
#
database = r'puge.db'
#
sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (104) NOT NULL,
mark FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL ,
is_married BOOLEAN DEFAULT FALSE
);
'''
# DOUBLE(4,2)

connection = create_connektion(database)
if connection is not None:
    # create_table(connection, sql_create_table)
    # create_student(connection,('Бека',10.2,'пишу','2003-06-06',False))
    reed(connection)
    print('все работает')