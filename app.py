from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, email TEXT)')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
