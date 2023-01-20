from flask import Flask, render_template, redirect, request
from os.path import dirname, abspath, join
dir = dirname(abspath(__file__))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        with open("data/text.txt", "a+") as outfile:
            outfile.writelines(message+"\n")
        return redirect("/")
    if request.method == "GET":
        with open("data/text.txt", "r") as file:
            messages = file.readlines()
        return render_template("index.html", messages=messages)

@app.route("/jamsroute", methods=["GET", "POST"])
def jams_data():
    return "Morning"