# import sqlite3

# conn = sqlite3.connect('intrusions.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, timestamp TEXT, alert TEXT)''')

# def log_intrusion(alert):
#     c.execute("INSERT INTO logs (timestamp, alert) VALUES (datetime('now'), ?)", (alert,))
#     conn.commit()

# def fetch_logs():
#     c.execute("SELECT * FROM logs")
#     return c.fetchall()

import sqlite3

conn = sqlite3.connect('intrusions.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS intrusions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    prediction TEXT,
    features TEXT
)
''')

conn.commit()
conn.close()
print("✅ Database and 'intrusions' table created.")

def log_intrusion(prediction, features):
    conn = sqlite3.connect('intrusions.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO intrusions (timestamp, prediction, features)
        VALUES (datetime('now'), ?, ?)
    """, (prediction, str(features)))
    conn.commit()
    conn.close()

def fetch_logs():
    conn = sqlite3.connect('intrusions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, prediction, features FROM intrusions ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows