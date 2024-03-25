import sqlite3 as sql

con = sql.connect ('banco_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOME" TEXT,
    "IDADE" TEXT,
    "RUA" TEXT,
    "CIDADE" TEXT,
    "NUMERO" TEXT,
    "ESTADO" TEXT
    )'''
cur.execute(sql)
con.commit()
con.close()