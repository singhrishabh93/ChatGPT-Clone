from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo

import openai

openai.api_key = "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"



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
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question" : question})
        print(chat)
        if chat:
            data = {"result": f"{chat['answer']}"}
            return jsonify(data)
        else:
            data = {"result": f"Answer of {question}"}
            response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    prompt=question,
                    messages=[
                        {
                        "role": "user",
                        "content": ""
                        }
                    ],
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
            mongo.db.chats.insert_one({"question" : question, "answer" : response})
            return jsonify(data)
    data = {"result": "Thanks"}
    return jsonify(data)

app.run(debug=True)