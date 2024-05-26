from flask import Flask 

# create an wsgi instance
app = Flask(__name__)

# Define the home route
@app.route("/")
@app.route("/home")
def home():
    return "<h1>HomePage</h1>"


@app.route("/about")
def about():
    return "<h1>AboutPage</h1>"
