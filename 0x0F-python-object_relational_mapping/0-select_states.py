#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, password=pwd, database=dbname)
    db = conn.cursor()
    db.execute("SELECT * FROM states;")
    data = db.fetchAll()
    print(data)
    conn.close()
