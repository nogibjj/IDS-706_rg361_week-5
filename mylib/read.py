"""
File to read data from a DB
"""

import sqlite3

def read_db(db_name="Master.db", table_name="Master", query=None):
    """
    Read from a DB, if no query is provided, it will return the first 5 rows
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    if query==None:
        query = "SELECT * FROM "+table_name +" LIMIT 5;"

    try:
        c.execute(query)
        payload = c.fetchall()
    except Exception:
        payload = "Invalid Query"
    conn.close()
    return payload

if __name__ == "__main__":
    print(read_db())
    pass