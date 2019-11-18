from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=False, nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return "User('{}.format({self.username})', '{}.format({self.email})', '{}.format{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return "Post('{}'.format({self.title}), '{}'.format({self.date_posted})"
    

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
    
if __name__ == '__main__':
    app.run(debug=True)
