import sqlite3

conn = sqlite3.connect("logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(
id INTEGER PRIMARY KEY,
timestamp TEXT,
event_type TEXT,
source_ip TEXT,
severity TEXT,
classification TEXT,
raw_log TEXT
)
""")

conn.commit()


def save_log(data, classification):

    cursor.execute("""
    INSERT INTO logs(timestamp,event_type,source_ip,severity,classification,raw_log)
    VALUES(?,?,?,?,?,?)
    """,(
        data.get("timestamp"),
        data.get("event_type"),
        data.get("source_ip"),
        data.get("severity"),
        classification,
        data.get("raw_log")
    ))

    conn.commit()