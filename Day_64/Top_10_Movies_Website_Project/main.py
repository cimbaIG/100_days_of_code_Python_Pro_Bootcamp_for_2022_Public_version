from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from matplotlib.pyplot import title
import sqlalchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = ""

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap(app)

class RateMovieForm(FlaskForm):
    cafe = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    location = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField('Done')

class MovieTitle(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(100), nullable=True)
    img_url = db.Column(db.String(300), nullable=False)

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"  
# )
# db.session.add(new_movie)
# db.session.commit()

def read_from_database():
    movies_in_db = db.session.query(Movie).all()
    return movies_in_db

def update_movie_info(movie_id, rating, review):
    movie_to_update = Movie.query.get(movie_id)
    movie_to_update.rating = rating
    movie_to_update.review = review
    db.session.commit()

def delete_movie_from_database(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

def add_movie_to_database(title, img_url, year, description):
    new_movie = Movie(title=title, img_url=img_url, year=year, description=description)
    db.session.add(new_movie)
    db.session.commit()
    return new_movie.id

def search_for_movies(title):
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query='+title)
    return response.json()

def get_movie_data(id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=en-US')
    return response.json()

@app.route("/")
def home():
    all_movies = read_from_database()
    all_movies = Movie.query.order_by(Movie.rating.asc()).all()
    n = len(all_movies)
    for movie in all_movies:
        movie.ranking = n
        n -= 1
    return render_template('index.html', movies=all_movies)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    rate_movie_form = RateMovieForm()
    if rate_movie_form.validate_on_submit():
        if request.method == 'POST':
            data_list = list(rate_movie_form.data.values())
            rating, review = data_list[0], data_list[1]
            movie_id = request.args.get('id')
            update_movie_info(movie_id=movie_id, rating=rating, review=review)
            return redirect(url_for('home'))
    return render_template('edit.html', form=rate_movie_form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    delete_movie_from_database(movie_id=movie_id)
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_title = MovieTitle()
    if request.method == "POST":
        title = movie_title.data.get('title')
        movie_data = search_for_movies(title)
        return render_template('select.html', movies=movie_data)
    return render_template('add.html', form=movie_title)

@app.route('/select')
def select():
    movie_id = request.args.get('id')
    data = get_movie_data(id=movie_id)
    title = data['title']
    img_url = 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
    year = data['release_date'].split('-')[0]
    description = data['overview']
    db_id = add_movie_to_database(title=title, img_url=img_url, year=year, description=description)
    return redirect(url_for('edit', id=db_id))

if __name__ == '__main__':
    app.run(debug=True)