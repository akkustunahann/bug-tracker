# Bug Tracker Tool

A lightweight bug tracking web application developed using Python, Flask, and SQLite.

## Project Objective

The purpose of this project is to provide a simple system for reporting,
tracking, and managing software bugs.

Users will be able to create bug reports and developers will be able to
update their status throughout the development process.

## Bug Workflow

Created → In Progress → Done

## Technologies

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Git
- GitHub

## Database

The bug database contains the following fields:

- ID
- Title
- Description
- Reported By
- Status
- Created At

## Project Structure

```text
bug-tracker/
├── app.py
├── database.py
├── schema.sql
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── hsb-logo.jpeg
```

## How to Run

Clone the repository, create and activate a virtual environment, install the dependencies, and run the application:

```bash
git clone https://github.com/akkustunahann/bug-tracker
cd bug-tracker
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Then open the following address in your browser:
http://127.0.0.1:5000

## Features

- Create new bug reports
- View all bugs in a dashboard
- Update bug statuses from the user interface
- Status workflow: Created → In Progress → Done
- Input validation for empty fields
- Database error handling
- Simple and clean user interface

## Version Control

This project was developed using Git and GitHub.

The project uses:
- `main` for the stable version
- `develop` for integration
- feature branches for individual development tasks

Feature branches were merged into `develop` using pull requests, and the completed application was merged into `main`.