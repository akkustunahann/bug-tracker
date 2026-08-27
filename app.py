import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, flash, session

from database import (
    create_database,
    get_all_bugs,
    create_bug,
    update_bug_status,
    delete_bug,
    authenticate_user
)

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/login")

    bugs = get_all_bugs()

    return render_template(
        "index.html",
        bugs=bugs
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = authenticate_user(username, password)

        if user is None:
            flash("Invalid username or password.", "error")
            return redirect("/login")

        session["user_id"] = user["id"]
        session["username"] = user["username"]
        session["role"] = user["role"]

        flash("Login successful.", "success")

        return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out.", "success")

    return redirect("/login")

@app.route("/add", methods=["POST"])
def add_bug():

    if "user_id" not in session:
        flash("Please log in first.", "error")
        return redirect("/login")

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    reported_by = request.form.get("reported_by", "").strip()

    if not title or not description or not reported_by:
        flash("Please fill in all fields.", "error")
        return redirect("/")

    success = create_bug(
        title,
        description,
        reported_by
    )

    if not success:
        flash("A database error occurred. Please try again.", "error")
        return redirect("/")

    flash("Bug submitted successfully!", "success")

    return redirect("/")
    
@app.route("/update_status", methods=["POST"])
def update_status():

    if session.get("role") != "admin":
        flash("You are not authorized to update bug status.", "error")
        return redirect("/")

    bug_id = request.form["bug_id"]
    new_status = request.form["status"]

    success = update_bug_status(
        bug_id,
        new_status
    )

    if success:
        flash("Status updated successfully.", "success")
    else:
        flash("Status could not be updated.", "error")

    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():

    if session.get("role") != "admin":
        flash("You are not authorized to delete bugs.", "error")
        return redirect("/")

    bug_id = request.form["bug_id"]

    success = delete_bug(bug_id)

    if success:
        flash("Bug deleted successfully.", "success")
    else:
        flash("Bug could not be deleted.", "error")

    return redirect("/")

if __name__ == "__main__":

    create_database()

    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)