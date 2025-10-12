from flask import Flask, render_template, request, redirect, url_for, session
import os
import database_manager as dbHandler

app = Flask(__name__)
app.secret_key = "secret_key_here"

# Folder for profile uploads
app.config['UPLOAD_FOLDER'] = "static/uploads"
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# --- MAIN PAGES ---
@app.route("/", methods=["GET", "POST"])
def index():
    data = dbHandler.listPlants()  # fetch plants from DB
    return render_template("index.html", content=data)


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/posts")
def posts():
    return render_template("posts.html")


# --- AUTHENTICATION PAGES ---
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            return "Passwords do not match!"

        # Store in session temporarily
        session["username"] = username
        return redirect(url_for("dashboard", username=username))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Just redirect to dashboard for now
        username = session.get("username", "User")
        return redirect(url_for("dashboard", username=username))

    return render_template("login.html")


# --- DASHBOARD PAGE ---
@app.route("/dashboard/<username>")
def dashboard(username):
    profile_pic = session.get("profile_pic", url_for('static', filename='images/default-plant.jpg'))
    recommended_users = [
        {"name": "PetalPirate 🌸", "username": "@petalpirate", "image": url_for('static', filename='images/user1.jpg')},
        {"name": "SoilSurfer 🪴", "username": "@soilsurfer", "image": url_for('static', filename='images/user2.jpg')},
        {"name": "LeafItToMe 😎", "username": "@leafit", "image": url_for('static', filename='images/user3.jpg')}
    ]
    return render_template("dashboard.html", username=username, profile_pic=profile_pic, recommended_users=recommended_users)


# --- UPDATE PROFILE PAGE ---
@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    if request.method == "POST":
        new_username = request.form["username"]
        file = request.files.get("profile_pic")

        if file and file.filename != "":
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            session["profile_pic"] = url_for('static', filename=f'uploads/{file.filename}')

        session["username"] = new_username
        return redirect(url_for('dashboard', username=new_username))

    return render_template("update_profile.html", username=username)


# --- SAVE PROFILE (POPUP) ---
@app.route("/save_profile", methods=["POST"])
def save_profile():
    username = request.form["username"]
    file = request.files.get("profile_pic")

    if file and file.filename != "":
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        session["profile_pic"] = url_for('static', filename=f'uploads/{file.filename}')

    session["username"] = username
    return redirect(url_for("dashboard", username=username))


# --- EVENT DETAIL PAGE ---
@app.route("/event/<event_id>")
def event_detail(event_id):
    if event_id == "mediterranean-cooking-class":
        return render_template("event_detail.html")
    else:
        return "Event not found", 404


# --- RUN SERVER ---
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
