"""
Creates a new Sqlite3 Database by reading the CSV Data from the link
"""
import sqlite3
import csv
import os

def create(db_name="Master.db", dataset="https://github.com/Opensourcefordatascience/Data-sets/raw/master/automotive_data.csv"):
    
    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS {}".format(db_name))
    header = payload[0]
    c.execute("CREATE TABLE GroceryDB (id,general_name, count_products, ingred_FPro, avg_FPro_products, avg_distance_root, ingred_normalization_term, semantic_tree_name, semantic_tree_node)")
    #insert
    c.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "GroceryDB.db"