from app import my_app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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

@my_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # method=POST and passed all form validations
        flash('Login requested for user {}, remember me={}' \
            .format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign-In", form=form)
