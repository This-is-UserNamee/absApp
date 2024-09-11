from flask import Flask
from flask import render_template, request, redirect, url_for
import db
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

db.create_books_tablfrom flask import Flask
from flask import render_template, request, redirect, url_for
import db
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

db.create_months_table()

@app.route('/')
def index():
    
    monthN = request.args.get('monthN')
    
    con = sqlite3.connect(DATABASE)
    if monthN == 'month1':
        db_month = con.execute('SELECT * FROM month1').fetchall()
    elif monthN == 'month2':
        db_month = con.execute('SELECT * FROM month2').fetchall()
    elif monthN == 'month3':
        db_month = con.execute('SELECT * FROM month3').fetchall()
    elif monthN == 'month4':
        db_month = con.execute('SELECT * FROM month4').fetchall()
    elif monthN == 'month5':
        db_month = con.execute('SELECT * FROM month5').fetchall()
    elif monthN == 'month6':
        db_month = con.execute('SELECT * FROM month6').fetchall()
    elif monthN == 'month7':
        db_month = con.execute('SELECT * FROM month7').fetchall()
    elif monthN == 'month8':
        db_month = con.execute('SELECT * FROM month8').fetchall()
    elif monthN == 'month9':
        db_month = con.execute('SELECT * FROM month9').fetchall()
    elif monthN == 'month10':
        db_month = con.execute('SELECT * FROM month10').fetchall()
    elif monthN == 'month11':
        db_month = con.execute('SELECT * FROM month11').fetchall()
    else:
        db_month = con.execute('SELECT * FROM month12').fetchall()
    con.close()
    
    
    month = []
    for row in db_month:
        month.append({'name': row[0], 'reason': row[1]})
        
    return render_template(
        'index.html',
        month=month
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST'])
def register():
    reason = request.form['reason']
    name = request.form['name']
    month = request.form['month']
    
    con = sqlite3.connect(DATABASE)
    if month == '1':
        con.execute('INSERT INTO month1 VALUES(?, ?)', [name, reason])
    elif month == '2':
        con.execute('INSERT INTO month2 VALUES(?, ?)', [name, reason])
    elif month == '3':
        con.execute('INSERT INTO month3 VALUES(?, ?)', [name, reason])
    elif month == '4':
        con.execute('INSERT INTO month4 VALUES(?, ?)', [name, reason])
    elif month == '5':
        con.execute('INSERT INTO month5 VALUES(?, ?)', [name, reason])
    elif month == '6':
        con.execute('INSERT INTO month6 VALUES(?, ?)', [name, reason])
    elif month == '7':
        con.execute('INSERT INTO month7 VALUES(?, ?)', [name, reason])
    elif month == '8':
        con.execute('INSERT INTO month8 VALUES(?, ?)', [name, reason])
    elif month == '9':
        con.execute('INSERT INTO month9 VALUES(?, ?)', [name, reason])
    elif month == '10':
        con.execute('INSERT INTO month10 VALUES(?, ?)', [name, reason])
    elif month == '11':
        con.execute('INSERT INTO month11 VALUES(?, ?)', [name, reason])
    else:
        con.execute('INSERT INTO month12 VALUES(?, ?)', [name, reason])
    con.commit()
    con.close()
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run()
e()

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
