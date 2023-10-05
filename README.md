# CRUD Operations in SQLite DB using Python and CLI

[![CI](https://github.com/nogibjj/IDS-706_rg361_week-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS-706_rg361_week-5/actions/workflows/cicd.yml)

This repositroy contains files to perform CRUD (Create-Write-Update-Delete) operations in a ``SQLite`` Database using ``Python`` and ``CLI``

The base repo has been forked from [sqlite-lab](https://github.com/nogibjj/sqlite-lab) and modified as per requirements.

Forked on on 29-Sep-2023

## Overview

The repository has the ``main.py`` file which makes use of the files in the mylib folder to perform CRUD operations on a SQLite Database. The main.py file can be interacted via ``CLI`` (Command Line Interface) by the user.

The repositoty automatically ``**logs**`` all the queries which are executed in the ``query_logs`` file.

[!Schema](resources/schema.png)

#### Tasks:

* Fork this project and get it to run
* Make the query more useful and not a giant mess that prints to screen
* Convert the main.py into a command-line tool that lets you run each step independantly
* Fork this project and do the same thing for a new dataset you choose
* Make sure your project passes lint/tests and has a built badge
* Include an architectural diagram showing how the project works

#### Reflection Questions

* What challenges did you face when extracting, transforming, and loading the data? How did you overcome them?
* What insights or new knowledge did you gain from querying the SQLite database?
* How can SQLite and SQL help make data analysis more efficient? What are the limitations?
* What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
* If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?

##### Challenge Exercises

* Add more transformations to the data before loading it into SQLite. Ideas: join with another dataset, aggregate by categories, normalize columns.
* Write a query to find correlated fields in the data. Print the query results nicely formatted.
* Create a second table in the SQLite database and write a join query with the two tables.
* Build a simple Flask web app that runs queries on demand and displays results.
* Containerize the application using Docker so the database and queries can be portable


