from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if not session.get("name"):
        return redirect("/username")
    if request.method == "POST":    
        message = request.form.get("message")
        with open("data/messages.txt", "a+") as outfile:
            name = session.get("name")
            outfile.writelines(f"<{name}>: {message}\n")
        return redirect("/")
    if request.method == "GET":
        with open("data/messages.txt", "r") as file:
            messages = file.readlines()
        return render_template("index.html", messages=messages)

@app.route("/username", methods=["POST", "GET"])
def username():
    if request.method == "GET":
        return render_template("username.html")
    if request.method == "POST":
        session["name"] = request.form.get("username")
        return redirect("/")

@app.route("/jamsroute", methods=["POST", "GET"])
def jams():
    if request.method == "GET":
        return "jams3" #render_template("username.html")
    if request.method == "POST":
        #jamsdata = request.form.get("somedata")
        return "jams24" #redirect("/")

@app.route("/ai")
def ai():
    return render_template("ai.html")
