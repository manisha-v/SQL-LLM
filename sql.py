import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

table = '''
CREATE TABLE Students(name VARCHAR(30), class VARCHAR(10), marks INT, company VARCHAR(30))
'''

cursor.execute(table)

cursor.execute('''insert into Students values('Manisha', 'MCA', 90, 'Microsoft')''')
cursor.execute('''insert into Students values('HARSHIT', 'BTech', 80, 'Qualcomm')''')
cursor.execute('''insert into Students values('Naren', 'MSc', 75, 'Tractrix')''')
cursor.execute('''insert into Students values('Gunjan', 'Nursing', 82, 'CHO')''')
cursor.execute('''insert into Students values('Disha', 'BCA', 70, 'BLC')''')

print("the inserted records-")
df = cursor.execute('''select * from Students''')

for row in df:
    print(row)

connection.commit()
connection.close()
