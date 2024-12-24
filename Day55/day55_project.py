from flask import Flask
import random

app=Flask(__name__)
@app.route("/")
def guess_number_website():
    return '<h1>Guess a number between 0 and 9</h1>'\
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
the_number=random.randint(1,9)
@app.route("/<int:guess>")
def user_guess(guess):
    print(the_number)
    if guess > the_number:
        return '<h1 style="color:purple">Too High ,try again!</h1>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess<the_number:
        return '<h1 style="color:red">Too Low ,try again!</h1>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color:green">You Found Me!</h1>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__=="__main__":
    app.run(debug=True)
