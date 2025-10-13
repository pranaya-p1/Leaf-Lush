from flask import Flask, render_template, request, redirect, url_for, session
import os
import database_manager as dbHandler

# --- Ensure Flask runs from the same directory as this file ---
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Create Flask app with explicit folder locations ---
app = Flask(
    __name__,
    static_folder='static',      # tell Flask exactly where to find static files
    template_folder='templates'  # where to find HTML templates
)

app.secret_key = "secret_key_here"

# Folder for profile uploads
app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, "uploads")
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# --- COMBINED add_post ROUTE --- #
@app.route("/add_post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title")
        caption = request.form.get("caption")
        image = request.files.get("image")

        # Save uploaded image if present
        if image and image.filename != "":
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(upload_path)
            image_url = url_for('static', filename=f'uploads/{image.filename}')
        else:
            image_url = url_for('static', filename='images/default_post.jpg')

        # Store post temporarily in session for now
        session.setdefault("posts", [])
        session["posts"].append({
            "title": title,
            "caption": caption,
            "image": image_url
        })

        # Save post to database (you can uncomment this if you have database models)
        # new_post = Post(title=title, caption=caption, image=image_url, user_id=current_user.id)
        # db.session.add(new_post)
        # db.session.commit()

        return redirect(url_for("dashboard", username=session.get("username", "User")))

    return render_template("add_post.html")

@app.route('/add_plant', methods=['GET', 'POST'])
def add_plant():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        bio = request.form['bio']
        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_plant = Plant(name=name, age=age, bio=bio, image=filename, user_id=current_user.id)
        db.session.add(new_plant)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('add_plant.html')


@app.route('/gardening_event1')
def gardening_event1():
    return render_template("gardening_event1.html")

@app.route('/gardening_event2')
def gardening_event2():
    return render_template("gardening_event2.html")

@app.route('/gardening_event3')
def gardening_event3():
    return render_template("gardening_event3.html")


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



@app.route("/update_profile/<username>", methods=["GET", "POST"])
def update_profile(username):
    if request.method == "POST":
        new_username = request.form["username"]
        bio = request.form.get("bio", "")
        fun_fact = request.form.get("fun_fact", "")
        file = request.files.get("profile_pic")

        if file and file.filename != "":
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            session["profile_pic"] = url_for('static', filename=f'uploads/{file.filename}')

        session["username"] = new_username
        session["bio"] = bio
        session["fun_fact"] = fun_fact

        return redirect(url_for('dashboard', username=new_username))

    return render_template(
        "update_profile.html",
        username=username,
        bio=session.get("bio", ""),
        fun_fact=session.get("fun_fact", "")
    )


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
