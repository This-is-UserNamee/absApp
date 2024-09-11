import sqlite3

DATABASE = 'database.db'

def create_months_table():
    i = 0
    con = sqlite3.connect(DATABASE)
    while i < 12:
        i2 = i+1
        con.execute("CREATE TABLE IF NOT EXISTS month"+str(i2)+" ( id, name, reason)")
        i = i + 1
    con.close()