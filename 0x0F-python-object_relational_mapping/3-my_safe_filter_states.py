#!/usr/bin/python3
"""
Connects to a MySQL database and executes a query to
retrieve data from a table called "states"
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for state in rows:
        if state[1] == argv[4]:
            print(state)
