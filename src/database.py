import sqlite3

def init_db():
    conn = sqlite3.connect("emails.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sender TEXT, subject TEXT, url TEXT, phishing INTEGER)''')
    conn.commit()
    conn.close()

def insert_result(sender, subject, url, phishing):
    conn = sqlite3.connect("emails.db")
    c = conn.cursor()
    c.execute("INSERT INTO results (sender, subject, url, phishing) VALUES (?,?,?,?)",
              (sender, subject, url, phishing))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
