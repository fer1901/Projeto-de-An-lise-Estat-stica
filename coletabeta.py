import sqlite3 


conn = sqlite3.connect("coletabeta.db")


cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Sa1 (
		Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		DataSA1 timestamp,
		Fornecedor TEXT NOT NULL, 
		Fator1 NUMERIC NOT NULL, 
		Fator2 REAL NOT NULL, 
		Fator3 REAL NOT NULL, 
		Fator4 REAL NOT NULL, 
		Fator5 REAL NOT NULL, 
		Fator6 REAL NOT NULL, 
		Fator7 REAL NOT NULL, 
		Fator8 REAL NOT NULL, 		
		Fator9 REAL NOT NULL, 
		Fator10 REAL NOT NULL, 
		Fator11 REAL NOT NULL,
		ParametrodeQualidade1 REAL NOT NULL
);
''')

print("conectado ao banco de dados do SA1")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sa2 (
		Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
		Fator12 REAL NOT NULL, 
		Fator13 REAL NOT NULL,
		Fator14 REAL NOT NULL, 
		Fator15 REAL NOT NULL, 
		Fator16 REAL NOT NULL, 
		Fator17 REAL NOT NULL,
		Fator18 REAL NOT NULL,
		Fator19 REAL NOT NULL, 
		Fator20 REAL NOT NULL,
		Fator21 REAL NOT NULL,
		Fator22 REAL NOT NULL,
		SA1 REAL NOT NULL,
		ParametrodeQualidade2 REAL NOT NULL, 
		ParametrodeQualidade3 REAL NOT NULL,
		DataSA2 timestamp
);
''')

print("Conectado ao banco de dados do SA2b")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Sa3 (
		Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		Fator23 REAL NOT NULL,
		Fator24 REAL NOT NULL, 
		Fator25 REAL NOT NULL, 
		Fator26 REAL NOT NULL, 
		Fator27 REAL NOT NULL,
		Fator28 REAL NOT NULL,
		Fator29 REAL NOT NULL,
		ParametrodeQualidade4 REAL NOT NULL,
		ParametrodeQualidade5 REAL NOT NULL, 
		ParametrodeQualidade6 REAL NOT NULL,
		SA2 REAL NOT NULL,
		DataSA3 timestamp
);
''')

print("Conectado ao banco de dados do SA3b")

