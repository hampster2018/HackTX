from flask import Flask, g
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
app.config["DATABASE"] = "./backend_database.db"


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
