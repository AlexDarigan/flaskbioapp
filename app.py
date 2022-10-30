from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.get("/home")
@app.get("/")
def home():
    return render_template("home.html")


@app.get("/cv")
def cv():
    return render_template("cv.html")


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

# Tech Sub Page Routes
@app.get("/godot")
def godot():
    return render_template("godot.html")

@app.get("/compose")
def compose():
    return render_template("compose.html")

@app.get("/docker")
def docker():
    return render_template("docker.html")

if __name__ == "__main__":
    app.run(debug=True)
