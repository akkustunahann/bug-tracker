from flask import Flask, render_template, request, redirect

from database import (
    create_database,
    get_all_bugs,
    create_bug
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

    title = request.form["title"]
    description = request.form["description"]
    reported_by = request.form["reported_by"]

    create_bug(
        title,
        description,
        reported_by
    )

    return redirect("/")


if __name__ == "__main__":

    create_database()

    app.run(debug=True)