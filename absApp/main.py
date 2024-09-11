from flask import Flask
from flask import render_template, request, redirect, url_for
import db
import sqlite3
import datetime

DATABASE = 'database.db'

app = Flask(__name__)

db.create_months_table()

@app.route('/')
def index():
    current_month = datetime.datetime.now().month
    default_monthN = 'month'+str(current_month)
    monthN = request.args.get('monthN', default_monthN)
    con = sqlite3.connect(DATABASE)
    db_month = con.execute('SELECT * FROM '+monthN).fetchall()
    con.close()
    
    months = [[]]
    i = 1
    while i < 13:
        con = sqlite3.connect(DATABASE)
        db_month = con.execute('SELECT * FROM month'+str(i)).fetchall()
        con.close()
        month = []
        for row in db_month:
            month.append({'id': row[0], 'name': row[1], 'reason': row[2]})
        months.append(month)
        i = i + 1
        
    return render_template(
        'index.html',
        months=months
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
    month = str(request.form['month'])
    sql = 'INSERT INTO month'+month+' (name, reason) VALUES (?, ?)'
    con = sqlite3.connect(DATABASE)
    con.execute(sql, (name, reason))
    con.commit()
    con.close()
    return redirect(url_for('index', monthN = 'month'+month))
    
@app.route('/delete')
def delete():
    id = request.args.get('id')
    monthN = request.args.get('monthN')
    print(id)
    print(monthN)
    # con = sqlite3.connect(DATABASE)
    # con.execute('DELETE FROM '+monthN+' WHERE name="apple"')
    # con.commit()
    # con.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
