"""
Query Scripts Using SQLite and Python
"""

# Import libraries
import sqlite3
import pandas as pd

# Import Custom Libraries functions
from mylib.logs import write_log, clear_log


# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
query()