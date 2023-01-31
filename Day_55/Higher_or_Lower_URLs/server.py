from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def route_page():
    global rand_int
    rand_int = random.randint(0,9)
    return '<h1>Guess a number between 0 and 9</h1> \
            <img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp">'

@app.route('/<int:number>')
def guess_number(number):
    if number < rand_int:
        return '<h1 style="color:red">Too low, try again!</h1> \
            <img src="https://media.giphy.com/media/fvBEGznNx4VhchaIgb/giphy.gif">'
    elif number > rand_int:
        return '<h1 style="color:DarkMagenta">Too high, try again!</h1> \
            <img src="https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif">'
    else:
        return '<h1 style="color:green">You found me!</h1> \
            <img src="https://media.giphy.com/media/elsol3P5Jt2ASsxLva/giphy-downsized-large.gif">'

if __name__ == '__main__':
    app.run(debug=True)