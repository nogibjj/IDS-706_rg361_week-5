"""
Creates a new Sqlite3 Database by reading the CSV Data
"""
import sqlite3
import csv
import os

def create(db_name='Master.db', dataset="Master.csv", auto=True):
    
    #prints the full working directory and path
    print(os.getcwd())
    if auto:
        dataset = "./Data/{}".format(dataset)
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    for row in payload:
        header = row
        break
    col_names = ""
    for i in header:
        col_names += i + ", "
    col_names = col_names[:-2]
    col_names = col_names.replace("-", "_")
    col_holder = "("+ ("?,"*len(header))[:-1]+")"

    c.execute("DROP TABLE IF EXISTS Master")

    create_query = "CREATE TABLE Master ("+col_names+")"
    
    c.execute(create_query)

    
    #insert
    insert_query = "INSERT INTO Master VALUES "+col_holder
    c.executemany(insert_query, payload)
    conn.commit()
    conn.close()
    pass

if __name__ == "__main__":
    create()
    pass
