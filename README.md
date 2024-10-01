# CRUD Hack

This is a CRUD application built using Flask and SQLite. It allows users to perform CRUD operations on a database of books.

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/CyrilBaah/CRUD-Hack/badge)](https://scorecard.dev/viewer/?uri=github.com/CyrilBaah/CRUD-Hack)


## Technology Stack
- [Python](https://www.python.org/ "python")
- [Sqlite](https://www.sqlite.org/ "Sqlite")
- [Flask](https://flask.palletsprojects.com/en/3.0.x/ "Flask")

## How to set up locally
1. Clone the project.
```sh
 git clone https://github.com/CyrilBaah/CRUD-Hack.git
```
```sh
 cd CRUD-Hack
```
2. Create a virtualenv
```sh
 virtualenv env
 source env/bin/activate
```
3. Install the packages
```sh
 pip install -r requirements.txt
```
4. Start the Server
```sh
 python3 app.py 
```

## How to Interact with the Application API

### Create a New Book
```sh
curl -X POST http://localhost:5000/books -H "Content-Type: application/json" -d '{"title": "New Book", "author": "John Doe", "published_date": "2022-01-01"}'
```

### Read All Books
```sh
curl -X GET http://localhost:5000/books
```

### Read a Single Book
```sh
curl -X GET http://localhost:5000/books/<id>
```

### Update a Book
```sh
curl -X PUT http://localhost:5000/books/<id> -H "Content-Type: application/json" -d '{"title": "Updated Book", "author": "Jane Smith", "published_date": "2022-01-02"}'
```

### Delete a book
```sh
curl -X DELETE http://localhost:5000/books/<id>
```