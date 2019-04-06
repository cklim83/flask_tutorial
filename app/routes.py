from app import my_app
from flask import render_template

@my_app.route('/')
@my_app.route('/index')
def index():
    user = {'username': 'Caleb'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)
