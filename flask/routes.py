from flask import render_template, url_for, flash, redirect
from flask import app
from flask.forms import RegistrationForm, LoginForm
from flask.models import User, Post

posts = [
    { 
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'APRIL 20'
    },
    { 
        'author': 'Tommy Schafer',
        'title': 'Blog Post 10',
        'content': 'second post content',
        'date_posted': 'APRIL 25'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)
    
@app.route("/about")
def about():
    return render_template('about.html', posts = title)
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!' .format({form.username.data}), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)