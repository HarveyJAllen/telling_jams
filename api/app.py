from flask import Flask, render_template, redirect, request
from os.path import dirname, abspath, join
dir = dirname(abspath(__file__))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        with open("data/text.txt", "a") as outfile:
            outfile.writelines(message+"\n")
        return redirect("/")
    if request.method == "GET":
        f = open("text.txt", "w")
        f.write("Hello")
        f.close()
        f = open("text.txt", "r")
        print(f.read())
        f.close()
        # with open("data/text.txt", "r+") as file:
        #     messages = file.readlines()
        return render_template("index.html", messages="Hello")