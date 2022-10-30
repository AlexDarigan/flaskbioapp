from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/cv")
def cv():
    return render_template("cv.html")


@app.get("/home")
def home():
    # Redundant with index?
    return render_template("home.html")


@app.get("/interests")
def interests():
    return render_template("interests.html")


@app.get("/personal")
def personal():
    return render_template("personal.html")


@app.get("/tech")
def tech():
    return render_template("tech.html")


@app.get("/wat")
def wat():
    return redirect("https://github.com/alexdarigan/wat", 301)


if __name__ == "__main__":
    app.run(debug=True)
