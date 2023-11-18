#!/usr/bin/python3
"""
Connects to a MySQL database and executes a query to
retrieve data from a table called "states"
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(argv[4]).strip("'"))
    rows = cur.fetchall()
    for state in rows:
        print(state)
