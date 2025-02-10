from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import subprocess

app = Flask(__name__)

# DB initialization

def init_db():
    try:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
init_db()

# Call encrypt-test.py

def call_encrypt_test():
    encrypt_test_path = 'encrypt-test.py'
    subprocess.Popen(['python3', encrypt_test_path])
    print("encrypt-test.py executed successfully.")

# Routes

@app.route('/')
def index():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    products = c.fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add():
    try:
        name = request.form['name']
        price = request.form['price']
        print(f"Received form data: name={name}, price={price}")
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        conn.close()
        print(f"Product {name} added successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    return redirect(url_for('index'))
  

if __name__ == '__main__':
    call_encrypt_test()
    app.run(host='10.2.5.25' , port=5000, debug=True)
