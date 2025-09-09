import os
import sqlite3 as sql

# Build an absolute path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "data_source.db")

# Example: list all tables in the database
def listTables():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    data = cur.fetchall()
    con.close()
    return data

# Example: list all plants from the Plants table
def listPlants():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT photo, bio, fruits, funFact FROM Plants")
    data = cur.fetchall()
    con.close()
    return data


def listExtension():
    return listPlants()   # or listTables(), depending on what you want

