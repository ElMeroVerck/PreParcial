from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/index2")
def index2():
    return render_template("index2.html")


if __name__ == "__main__":
    app.run(debug=True)