from flask import Flask, render_template

datas = [
    {
        'title': "Blog post 1",
        'author': "Mehrab Hossain",
        'date_posted': 'May 26, 2024',
        'content': "First post content"
    },

    {
        'title': "Blog post 2",
        'author': "Zoti Hossain",
        'date_posted': 'May 26, 2024',
        'content': "Second post content"
    }
]

# create an wsgi instance
app = Flask(__name__)

# Define the home route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = datas)

@app.route("/about")
def about():
    return render_template('about.html', title="About")
