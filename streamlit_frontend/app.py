from flask import Flask, g, request
from flask_cors import CORS
import sqlite3
import pickle
from sklearn.neural_network import MLPClassifier
import openai
from dotenv import load_dotenv
import os
from config import prompts
from generateUniqueQuestions import generateUniqueQuestions
from generateQuestions import generateQuestions
from send_sms import send_SMS
from datetime import date
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

app.config["DATABASE"] = "./backend_database.db"
app.config["MODELPATH"] = "../model_code/finalized_model.sav"

dailyQuestions = []

load_dotenv()
openai.api_key = os.getenv("OPENAIAPIKEY")
openai.organization = os.getenv("OPENAIORGANIZATION")

loaded_model = pickle.load(open(app.config["MODELPATH"], "rb"))
authkey = os.getenv("AUTHKEY")
authRejectMessage = os.getenv("AUTHREJECTMESSAGE")


@app.before_request
def checkAPI():
    header = request.headers.get("Authorization")

    if header != authkey:
        return authRejectMessage


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        g._database = sqlite3.connect(app.config["DATABASE"])
        db = g._database
        with app.open_resource("schema.sql") as f:
            db.executescript(f.read().decode("utf8"))
        # if the database has nothing in the users, run the seed_database.sql file
        cur = db.cursor()
        cur.execute("SELECT * FROM users")
        output = cur.fetchall()
        if output == []:
            with app.open_resource("seed_database.sql") as f:
                db.executescript(f.read().decode("utf8"))
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def hello_world():
    get_db()
    return "Hello, World!"


@app.route("/setDailyQuestions", methods=["POST"])
def setDailyQuestions():
    global dailyQuestions

    form = request.form

    dte = date.today()

    dte = pd.to_datetime(dte.strftime("%Y-%m-%d"))

    if dte.dayofweek == 5:
        dailyQuestions = generateQuestions(form["question"], True)

    else:
        dailyQuestions = generateQuestions(form["question"], False)

    send_SMS()

    return "200"


@app.route("/postDailyAnswer", methods=["POST"])
def postDailyAnswer():
    form = request.form
    question = form["question"]
    answer = form["answer"]
    id = form["id"]

    print(question, answer, id)

    return "200"


@app.route("/getDailyQuestions")
def getDailyQuestions():
    global dailyQuestions
    return json.dumps(dailyQuestions)


@app.route("/postResponse/<id>", methods=["POST"])
def postResponse(id):
    form = request.form
    question = form["question"]
    answer = form["answer"]
    score = sentimentAnalysis(question, answer)
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO form_responses VALUES (?, ?)", (id, score))
    return score


@app.route("/serveModel")
def serve_model():
    data = [0.854096, 0.985810, 0, 0, 0]

    prediction = loaded_model.predict([data])

    return str(prediction[0])


@app.route("/getQuestions")
def getQuestions():
    try:
        response = generateUniqueQuestions()
    except Exception as e:
        response = [
            "How was your morning today?",
            "How is your family doing?",
            "How is your job going?",
        ]

    return response


def sentimentAnalysis(question, answer):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Give only a number response from 1-100 on how positive you would rate the response to the question: "
                + question,
            },
            {"role": "user", "content": answer},
        ],
        max_tokens=300,
        temperature=0.7,
        top_p=1,
    )

    return str(int(completion["choices"][0]["message"]["content"]) / 100)
