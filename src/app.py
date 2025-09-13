from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask backend is running! Go to /emails to see results."

@app.route("/emails")
def get_emails():
    conn = sqlite3.connect("emails.db")
    c = conn.cursor()
    c.execute("SELECT sender, subject, url, phishing FROM results")
    rows = c.fetchall()
    conn.close()
    data = [
        {"sender": r[0], "subject": r[1], "url": r[2], "phishing": bool(r[3])}
        for r in rows
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
