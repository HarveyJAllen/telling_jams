from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message")
        with open("./api/static/messages.txt", "a") as outfile:
            outfile.writelines(message+"\n")
        return redirect("/")
    if request.method == "GET":
        # with open("./api/static/messages.txt", "r+") as file:
        #     messages = file.readlines()
        return render_template("index.html", messages=messages)
