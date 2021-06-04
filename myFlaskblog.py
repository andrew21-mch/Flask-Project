from flask import Flask, render_template
app  = Flask(__name__)

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
    return render_template('home.html', posts=posts)

@app.route("/about")
def About():
    return render_template('about.html', title = "about page")

if __name__ == '__main__':
    app.run(debug=True)