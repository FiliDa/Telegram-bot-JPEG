import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), 'bot_database.db')

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT id,audience,status,offset,total FROM broadcast_jobs WHERE status='running'")
    rows = cur.fetchall()
    print("running_before=", rows)
    cur.execute("UPDATE broadcast_jobs SET status='stopped' WHERE status='running'")
    con.commit()
    cur.execute("SELECT id,audience,status,offset,total FROM broadcast_jobs ORDER BY id DESC LIMIT 20")
    print("tail_after=", cur.fetchall())
    con.close()

if __name__ == "__main__":
    main()
