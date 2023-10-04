"""
File to read data from a DB
"""

import sqlite3

def read_db(db_name="Master.db", table_name="Master", columns="*"):
    """
    Read from a DB
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT {} FROM {}".format(columns, table_name))
    payload = c.fetchall()
    conn.close()
    return payload

if __name__ == "__main__":
    print(read_db())
    pass