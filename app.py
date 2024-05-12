from flask import Flask, request, jsonify
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

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        data = read_data()
        return jsonify(data)
    elif request.method == 'POST':
        data = request.get_json()
        insert_data(data['title'], data['author'], data['published_date'])
        return 'Data inserted successfully!'

@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        # Retrieve a single book by ID
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM books WHERE id=?''', (id,))
        data = c.fetchone()
        conn.close()
        return jsonify(data)
    elif request.method == 'PUT':
        # Update a book by ID
        data = request.get_json()
        update_data(id, data['title'], data['author'], data['published_date'])
        return 'Data updated successfully!'
    elif request.method == 'DELETE':
        # Delete a book by ID
        delete_data(id)
        return 'Data deleted successfully!'

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
