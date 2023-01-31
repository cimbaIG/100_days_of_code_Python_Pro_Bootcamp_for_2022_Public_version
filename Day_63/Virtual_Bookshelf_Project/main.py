from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

# all_books = []

def add_to_database(title, author, rating):
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()

def read_from_database():
    books_in_db = db.session.query(Book).all()
    return books_in_db

def update_book_rating(book_id):
    book_to_update = Book.query.get(book_id)
    book_to_update.rating = request.form["rating"]
    db.session.commit()

def delete_book_from_database(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

@app.route('/')
def home():
    all_books = read_from_database()
    return render_template('index.html', books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":       
        # all_books.append(request.form.to_dict())
        add_to_database(title=request.form.to_dict()['title'], author=request.form.to_dict()['author'], rating=request.form.to_dict()['rating'])
        # After the book is added redirect to the home page.
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit_rating", methods=['GET', 'POST'])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        update_book_rating(book_id)
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete_book")
def delete_book():
    id = request.args.get('id')
    delete_book_from_database(book_id=id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)