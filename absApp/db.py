import sqlite3

DATABASE = 'database.db'

def create_months_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS month1 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month2 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month3 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month4 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month5 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month6 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month7 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month8 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month9 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month10 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month11 (name, reason)")
    con.execute("CREATE TABLE IF NOT EXISTS month12 (name, reason)")
    con.close()