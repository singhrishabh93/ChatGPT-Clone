from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://singhrishabh1670:Re%40lmeBook@gptclone.31q8ngu.mongodb.net/chatgpt"
mongo = PyMongo(app)
app = Flask(__name__)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats = myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method== "POST":
        data = {"result": "Hey"}
        return jsonify(data)
    data = {"result": "Hey"}
    return jsonify(data)

app.run(debug=True)