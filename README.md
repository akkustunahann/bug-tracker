# Bug Tracker Tool

A lightweight bug tracking web application developed using Python, Flask, and SQLite.

## Project Objective

The purpose of this project is to provide a simple system for reporting, tracking, and managing software bugs.

Users can create bug reports, while authorized users can update their status and manage completed bugs.

## Bug Workflow

Created → In Progress → Done

## Technologies

- Python
- Python-dotenv
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Git
- GitHub

## Database

The application uses SQLite and contains the following main tables:

### Bugs

- ID
- Title
- Description
- Reported By
- Status
- Created At

### Users

- ID
- Username
- Password Hash
- Role

### Activity Logs

- ID
- User ID
- Username
- Action
- Bug ID
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
    └── login.html
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
```

Create a .env file in the project root and add:
```bash
SECRET_KEY=your-secret-key
FLASK_DEBUG=true
```

Then run the application:
```bash
python app.py
```

Then open the following address in your browser:
http://127.0.0.1:5000

## Features

- Create new bug reports
- View all bugs in a dashboard
- User authentication with secure password hashing
- Role-based authorization
- Admin-only status updates
- Admin-only deletion of completed bugs
- Status workflow: Created → In Progress → Done
- Activity logging for user actions
- Server-side success and error messages using Flask flash
- Input validation for empty fields
- Database error handling
- Environment-based configuration
- Simple HSB-branded user interface

## Version Control

This project was developed using Git and GitHub.

The project uses:
- `main` for the stable version
- `develop` for integration
- feature branches for individual development tasks

Feature branches were merged into `develop` using pull requests, and the completed application was merged into `main`.