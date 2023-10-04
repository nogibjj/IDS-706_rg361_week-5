"""
Creates a new Sqlite3 Database by reading the CSV Data
"""
import sqlite3
import csv
import os

def create(db_name="Master.db", dataset="Master.csv", auto=True):
    
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
    col_holder = "("+ ("?,"*len(header))[:-1]+")"

    #c.execute("DROP TABLE IF EXISTS {}".format(db_name))

    create_query = "CREATE TABLE MasterDB ("+col_names+")"
    print(create_query)
    
    # c.execute("CREATE TABLE MasterDB ("+col_names+")")

    # #insert
    # c.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    # conn.commit()
    # conn.close()
    # return "GroceryDB.db"

if __name__ == "__main__":
    create()
    pass
