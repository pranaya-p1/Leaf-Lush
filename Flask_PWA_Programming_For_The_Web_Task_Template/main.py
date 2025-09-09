from flask import Flask, render_template, request
import database_manager as dbHandler

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    # fetch plants from DB (change to listTables() if you only want to test tables)
    data = dbHandler.listPlants()
    return render_template("index.html", content=data)

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

