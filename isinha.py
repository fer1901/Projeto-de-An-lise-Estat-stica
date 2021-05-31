import sqlite3 


conn = sqlite3.connect("banconovo.db")


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Call (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL, 
    Data TIMESTAMP,
    CPF REAL NOT NULL
);
''')

print("funcionou")
