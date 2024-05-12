from flask import Flask
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, published_date TEXT)''')
    conn.commit()
    conn.close()

def insert_data(title, author, published_date):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO books (title, author, published_date) VALUES (?, ?, ?)''', (title, author, published_date))
    conn.commit()
    conn.close()

def read_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM books''')
    data = c.fetchall()
    conn.close()
    return data

def update_data(id, title, author, published_date):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''UPDATE books SET title=?, author=?, published_date=? WHERE id=?''', (title, author, published_date, id))
    conn.commit()
    conn.close()

def delete_data(id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''DELETE FROM books WHERE id=?''', (id,))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return 'Welcome to the CRUD app!'

@app.route('/create')
def create():
    create_table()
    return 'Table created successfully!'

@app.route('/insert')
def insert():
    insert_data('Book Title', 'Author Name', '2022-01-01')
    return 'Data inserted successfully!'

@app.route('/read')
def read():
    data = read_data()
    return str(data)

@app.route('/update')
def update():
    update_data(1, 'Updated Title', 'Updated Author', '2022-01-02')
    return 'Data updated successfully!'

@app.route('/delete')
def delete():
    delete_data(1)
    return 'Data deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
