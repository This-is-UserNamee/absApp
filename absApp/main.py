from flask import Flask
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
    db_month = con.execute('SELECT * FROM '+monthN).fetchall()
    con.close()
    
    
    month = []
    for row in db_month:
        month.append({'id': row[0], 'name': row[1], 'reason': row[2]})
        
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
    con.execute('INSERT INTO month'+str(month)+' VALUES(1, ?, ?)', [name, reason])
    con.commit()
    con.close()
    return redirect(url_for('index', monthN = 'month'+month))
    
# @app.route('/delete')
# def delete():
#     number = request.args.get('number')
#     monthN = request.args.get('monthN')
#     con = sqlite3.connect(DATABASE)
#     con.execute('DELETE FROM '+monthN+' WHERE name="apple"')
#     con.commit()
#     con.close()
#     return redirect(url_for('index',monthN=monthN))

if __name__ == '__main__':
    app.run()
