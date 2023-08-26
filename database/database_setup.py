import sqlite3
import pathlib
import os

def create_database():
    db_dir = os.path.join(pathlib.Path(__file__).parent)
    db_file = os.path.join(db_dir, "data.db")

    if os.path.isfile(db_file):
        print("WARNING: A database file \"data.db\" already exists and will be overwritten.")
        answer = input("Are you sure you want to continue (Y/n): ")

        if answer != "Y":
            print("Creation of database aborted")
            return
        else:
            os.remove(db_file)

    ## Create the db file
    with open(db_file, "w"): pass

    db = sqlite3.connect("./data.db")

    with open(os.path.join(db_dir, "create.sql")) as f:
        script = f.read()

    cursor = db.cursor()
    cursor.executescript(script)

    db.commit()
    db.close()

create_database()
