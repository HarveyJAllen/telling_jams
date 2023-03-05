from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import threading
import socket

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
        if message.lower() in ["muppet", "muppet ", ]:
            return render_template("muppet.html")
        if message.lower() in ["rick roll", "rick roll ", "rickroll", "rickroll "]:
            with open("data/messages.txt", "r") as file:
                messages = file.readlines()
            return render_template("index.html", messages=messages, rickroll=True)
        with open("data/messages.txt", "a+") as outfile:
            name = session.get("name")
            outfile.writelines(f"<{name}>: {message}\n")
        return redirect("/")
    if request.method == "GET":
        with open("data/messages.txt", "r") as file:
            messages = file.readlines()
        #return render_template("foxypink.html")
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
        with open("data/messages.txt", "r") as file:
            messages = file.readlines()
        return messages
        #return "jams33" #render_template("username.html")
    if request.method == "POST":
        #jamsdata = request.form.get("somedata")
        return "jams243" #redirect("/")

@app.route("/ai")
def ai():
    return render_template("ai.html")

host = "0.0.0.0"
port = 443

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

somevar = 5
somevar += 1

clients = []
aliases = []
msglist = []

def broadcast(msg):
    msglist.append((msg + '\n').encode('utf-8'))
    for client in clients:
        client.send(msg.encode('utf-8'))

def handle_client(client):
    alias = client.recv(14).decode('utf-8')
    aliases.append(alias)
    clients.append(client)

    for msg in msglist:
        client.send(msg)

    broadcast(f'<{alias} has joined the chat>')

    while True:
        try:
            msg = client.recv(255).decode('utf-8')
            index = clients.index(client)
            alias = aliases[index]
            broadcast(f"<{alias}>: {msg}")
            #add to file so can be displayed on webpage
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"<{alias} has left the chat>")
            aliases.remove(alias)
            break

def receice_app_client():
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    thread = threading.Thread(target=receice_app_client)
    thread.start()
    app.run(debug=False, host="0.0.0.0", port="80")
