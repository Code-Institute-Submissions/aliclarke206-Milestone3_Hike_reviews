import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_hikes")
def get_hikes():
    hikes = mongo.db.hikes.find()
    return render_template("hikes.html", hikes=hikes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    hikes = list(mongo.db.hikes.find({"$text": {"$search": query}}))
    return render_template("hikes.html", hikes=hikes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_hike", methods=["GET", "POST"])
def add_hike():
    if request.method == "POST":
        is_parking = "on" if request.form.get("is_parking") else "off"
        hike = {
            "county_name": request.form.get("county_name"),
            "hike_name": request.form.get("hike_name"),
            "hike_description": request.form.get("hike_description"),
            "is_parking": is_parking,
            "hike_difficulty": request.form.get("hike_difficulty"),
            "hike_duration": request.form.get("hike_duration"),
            "created_by": session["user"]
        }
        mongo.db.hikes.insert_one(hike)
        flash("Hike Successfully Added")
        return redirect(url_for("get_hikes"))

    return render_template("add_hike.html")


@app.route("/edit_hike/<hike_id>", methods=["GET", "POST"])
def edit_hike(hike_id):
    if request.method == "POST":
        is_parking = "on" if request.form.get("is_parking") else "off"
        submit = {
            "county_name": request.form.get("county_name"),
            "hike_name": request.form.get("hike_name"),
            "hike_description": request.form.get("hike_description"),
            "is_parking": is_parking,
            "hike_difficulty": request.form.get("hike_difficulty"),
            "hike_duration": request.form.get("hike_duration"),
            "created_by": session["user"]
        }
        mongo.db.hikes.update({"_id": ObjectId(hike_id)}, submit)
        flash("Hike Successfully Updated")

    hike = mongo.db.hikes.find_one({"_id": ObjectId(hike_id)})
    return render_template("edit_hike.html", hike=hike)


@app.route("/delete_hike/<hike_id>")
def delete_hike(hike_id):
    mongo.db.hikes.remove({"_id": ObjectId(hike_id)})
    flash("Hike Successfully Deleted")
    return redirect(url_for("get_hikes"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)