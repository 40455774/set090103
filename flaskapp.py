from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '12345'

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
        flash('Account created for {}!' .format({form.username.data}))
    return render_template('register.html', title="Register", form=form)
    
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)
    
    

if __name__ == '__main__':
    app.run(debug=True)
