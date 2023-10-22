import sqlite3


if __name__ == "__main__":
    # get the database
    db = sqlite3.connect("./backend_database.db")

    # drop all tables
    db.execute("DROP TABLE IF EXISTS users")
    db.execute("DROP TABLE IF EXISTS form_responses")
    db.execute("DROP TABLE IF EXISTS questions")
    db.commit()

    # open the "schema.sql" file
    with open("schema.sql") as f:
        db.executescript(f.read())

    # if the database has nothing in the users, run the seed_database.sql file
    with open("seed_database.sql") as f:
        db.executescript(f.read())

    # close the database
    db.close()
