from flask import Flask, render_template, request, redirect, url_for
import database_manager as dbHandler

app = Flask(__name__)

# --- Main Pages ---
@app.route("/", methods=["GET", "POST"])
def index():
    data = dbHandler.listPlants()  # fetch plants from DB
    return render_template("index.html", content=data)

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")

# --- Auth Pages ---
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # TODO: Save to DB instead of this dummy check
        if password == confirm_password:
            return redirect(url_for("login"))
        else:
            return "Passwords do not match!"

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # TODO: Replace with DB validation
        return redirect(url_for("dashboard"))

    return render_template("login.html")

# --- Run Server ---
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
