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

loaded_model = pickle.load(open(app.config["MODELPATH"], 'rb'))
authkey = os.getenv("AUTHKEY")
authRejectMessage = os.getenv("AUTHREJECTMESSAGE")

@app.before_request
def checkAPI():
    
    header = request.headers.get("Authorization")

    if header != authkey:
        return authRejectMessage, 401


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
    print(dte.dayofweek)
                         
    if dte.dayofweek == 5:
        dailyQuestions = generateQuestions(form['question'][1:-2], True)

    else:
        dailyQuestions = generateQuestions(form['question'][1:-2], False)

    print(dailyQuestions)

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

    return sentimentAnalysis(question, answer)

@app.route("/serveModel")
def serve_model():
    data = [0.854096, 0.985810, 0, 0, 0]

    prediction = loaded_model.predict([data])

    return str(prediction[0])

@app.route("/getQuestions")
def getQuestions():
    return generateUniqueQuestions()

##@app.route("/sendSMS", methods=["GET"])
##def sendSMS():
##    send_SMS()
##    return "200"

def sentimentAnalysis(question, answer):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Give only a number response from 1-100 on how positive you would rate the response to the question: " + question},
            {"role": "user", "content": answer},
        ],
        max_tokens=300,
        temperature=0.7,
        top_p=1,
    )

    return str(int(completion['choices'][0]['message']['content']) / 100)

    