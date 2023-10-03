"""
Module to Get data from links and save as csv file locally and delete them if requried
"""

import requests
import os

def create_data(source="https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/main/data/GroceryDB_IgFPro.csv", 
            file_name="Master.csv", auto=True):
    """"Extract a url to a file path"""
    if auto:
        filepath = "./Data/{}".format(file_name)
    else:
        filepath = file_name

    print(filepath)
    with requests.get(source) as r:
        with open(filepath, 'wb') as f:
            f.write(r.content)
    pass

def delete_data(file_name="Master.csv", auto=True):
    """"Delete a file path"""
    if auto:
        file_path = "Data/{}".format(file_name)
    else:
        file_path = file_name
    os.remove(file_path)
    pass

if __name__ == "__main__":
    delete_data()
    pass