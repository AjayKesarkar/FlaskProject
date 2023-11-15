from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/signin")
def signin():
    return render_template("sign_in.html")

@app.route("/forget_pass")
def reset_pass():
    return render_template("forget_pass.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run()