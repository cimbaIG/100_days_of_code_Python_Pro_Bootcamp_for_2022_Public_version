from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = ""
PASSWORD = ""

API_URL = ""
response = requests.get(API_URL)
blog_posts = response.json()

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(MY_EMAIL, "", email_message)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blog_posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:id>')
def post(id):
    for blog_post in blog_posts:
        if blog_post['id'] == id:
            return render_template("post.html", id=blog_post['id'], blog_post=blog_post)

if __name__ == '__main__':
    app.run(debug=True)