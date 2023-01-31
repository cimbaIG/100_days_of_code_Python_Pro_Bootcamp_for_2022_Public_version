from flask import Flask, render_template
import requests

API_URL = "https://api.npoint.io/0815725477c7567c8d22"
response = requests.get(API_URL)
blog_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blog_posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    for blog_post in blog_posts:
        if blog_post['id'] == id:
            return render_template("post.html", id=blog_post['id'], blog_post=blog_post)

if __name__ == '__main__':
    app.run(debug=True)