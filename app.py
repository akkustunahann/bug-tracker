from flask import Flask, render_template, request, redirect

from database import (
    create_database,
    get_all_bugs,
    create_bug,
    update_bug_status,
    delete_bug
)


app = Flask(__name__)


@app.route("/")
def home():

    bugs = get_all_bugs()

    return render_template(
        "index.html",
        bugs=bugs
    )


@app.route("/add", methods=["POST"])
def add_bug():

    title = request.form["title"].strip()
    description = request.form["description"].strip()
    reported_by = request.form["reported_by"].strip()

    if not title or not description or not reported_by:
        bugs = get_all_bugs()

        return render_template(
            "index.html",
            bugs=bugs,
            error="Please fill in all fields."
        )

    success = create_bug(
        title,
        description,
        reported_by
    )

    if not success:
        bugs = get_all_bugs()

        return render_template(
            "index.html",
            bugs=bugs,
            error="A database error occurred. Please try again."
        )

    return redirect("/")
    

@app.route("/update_status", methods=["POST"])
def update_status():

    bug_id = request.form["bug_id"]
    new_status = request.form["status"]

    success = update_bug_status(
        bug_id,
        new_status
    )

    if not success:
        bugs = get_all_bugs()

        return render_template(
            "index.html",
            bugs=bugs,
            error="Status could not be updated."
        )

    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    bug_id = request.form["bug_id"]

    delete_bug(bug_id)

    return redirect("/")

if __name__ == "__main__":

    create_database()

    app.run(debug=True)