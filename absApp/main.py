from flask import Flask
from flask import render_template, request, redirect, url_for
import db
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

db.create_books_table()

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT * FROM books').fetchall()
    con.close()
    
    books = []
    for row in db_books:
        books.append({'month': row[0], 'reason': row[1], 'name': row[2]})
        
    return render_template(
        'index.html',
        books=books
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST'])
def register():
    month = request.form['month']
    reason = request.form['reason']
    name = request.form['name']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books VALUES(?, ?, ?)',
                [month, reason, name])
    con.commit()
    con.close()
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run()
