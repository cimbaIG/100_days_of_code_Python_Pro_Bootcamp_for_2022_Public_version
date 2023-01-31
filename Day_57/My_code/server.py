from unicodedata import name
from flask import Flask, render_template
import random
from datetime import date
import requests

AGIFY_URL = "https://api.agify.io?name="
GENDERIZE_URL = "https://api.genderize.io?name="

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = date.today().year
    return render_template("index.html", num=random_number, current_year=year)

@app.route('/guess/<string:name>')
def guess(name):
    gender_response = requests.get(url=GENDERIZE_URL+name)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    age_response = requests.get(url=AGIFY_URL+name)
    age_response.raise_for_status()
    age_data = age_response.json()
    return render_template("guess.html", name=name, gender=gender_data['gender'], age=age_data['age'])

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://www.npoint.io/docs/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)