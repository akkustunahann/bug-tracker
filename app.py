import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, flash

from database import (
    create_database,
    get_all_bugs,
    create_bug,
    update_bug_status,
    delete_bug
)

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def home():

    bugs = get_all_bugs()

    return render_template(
        "index.html",
        bugs=bugs
    )


@app.route("/add", methods=["POST"])
def add_bug():

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