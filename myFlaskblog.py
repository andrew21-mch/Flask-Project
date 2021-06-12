from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app  = Flask(__name__)

app.config['SECRET_KEY'] = 'e476fb0ba1f350ff199a8bacb01368ea';

posts = [
    {
        'author': 'Andrew',
        'title': 'Blog Post 1',
        'content': "First Posted content",
        'date_posted': 'June 4, 2021'
    },
    {
        'author': 'Jude Mani',
        'title': 'Blog Post 2',
        'content': "Second Posted content",
        'date_posted': 'June 13, 2021'
    },



]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="home", posts=posts)

@app.route("/about")
def About():
    return render_template('about.html', title = "about page")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)