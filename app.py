from flask import Flask, render_template

# create an wsgi instance
app = Flask(__name__)

# Define the home route
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')
