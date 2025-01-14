#Sample File for coding practice.
from flask import Flask
import random

app = Flask(__name__)
print(__name__)
random_number = random.randint(0, 9)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


@app.route("/<int:guess>")
def user_guess(guess):
    if guess < random_number:
        return '<h1>Number is too low!. Guess Higher!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy-downsized-large.gif" width=200>'

    elif guess == random_number:
        return '<h1>You''' + 've guessed it correct!</h1>' \
                             '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'

    else:
        return '<h1>Number is too high. Guess again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'


if __name__ == "__main__":
    app.run(debug=True)
