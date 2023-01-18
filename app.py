from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.method == "GET":
        return "aaaaaa"
    if request.method == "POST":
        return "eeeeee"