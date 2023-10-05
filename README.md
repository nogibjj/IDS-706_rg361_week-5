# CRUD Operations in SQLite DB using Python and CLI

[![CI](https://github.com/nogibjj/IDS-706_rg361_week-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS-706_rg361_week-5/actions/workflows/cicd.yml)

This repositroy contains files to perform CRUD (Create-Write-Update-Delete) operations in a ``SQLite`` Database using ``Python`` and ``CLI``

The base repo has been forked from [sqlite-lab](https://github.com/nogibjj/sqlite-lab) and modified as per requirements.

Forked on on 29-Sep-2023

## Overview

The repository has the ``main.py`` file which makes use of the files in the mylib folder to perform CRUD operations on a SQLite Database. The main.py file can be interacted via ``CLI`` (Command Line Interface) by the user.

The repositoty automatically **``logs``** all the queries which are executed in the ``query_logs`` file.

``Github`` actions automatically runs the ``test_main.py`` whenever there is an update in the repository which automatically performs all the default operations. 

![Schema](resources/schema.png)

