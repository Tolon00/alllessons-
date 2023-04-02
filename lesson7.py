# SQL-язык бд
# СУБД- субд 2вида

import sqlite3

# CRUD-create
# read
# update
# delete
db = sqlite3.connect('test.db')
c = db.cursor() #курсор нужен для того чтобы выполнять основные команды sql
c.execute('''CREATE TABLE IF NOT EXISTS
user(
name TEXT,
age INTEGER,
view BOOLEAN,
lastname TEXT
)''')

# c.execute('INSERT INTO user VALUES ("Мирлан",16,10,"Dreemann")')
# c.execute('INSERT INTO user VALUES ("EМирлан",06,10,"Белетбеков")')

# c.execute('INSERT INTO user VALUES ("Мирлан",16,10,"Dreemann")')
# c.execute('INSERT INTO user VALUES ("EМирлан",06,10,"Белетбеков")')

# c.execute('INSERT INTO user VALUES ("Мирлан",16,10,"Dreemann")')
# c.execute('INSERT INTO user VALUES ("EМирлан",06,10,"Белетбеков")')


# c.execute("UPDATE user SET name='Ахмат' WHERE name='EМирлан' ")
# c.execute("UPDATE user SET name='Садыр' WHERE name='Ахмад'")
# c.execute("UPDATE user SET lastname='GOOGle' WHERE rowid>1 ")
# c.execute("UPDATE user SET name='Ахмат' WHERE rowid=1 ")
c.execute("DELETE FROM user WHERE rowid>1")
# c.execute("DELETE FROM user WHERE rowid<>0")


c.execute("SELECT rowid,* FROM user") #rowid чтобы достать свои id
item = c.fetchall() #достает всех
for i in item:
    print(i)
print(c.fetchone()) #достает первую
print(c.fetchmany(4)) #достает сколько указано
db.commit() #сохранение
db.close()




# git checkout master(tolon) - изменение ветки
# git merge tolon(master) - слияет ветку
# git checkout -b test(kdjfk) - создает новую ветку и слияет предыдущую ветку и переключиться на новую
