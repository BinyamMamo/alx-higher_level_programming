#!/usr/bin/python3
"""
lists all states with a name starting with N
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    con = MySQLdb.connect(host="localhost",
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3])
    cur = con.cursor()

    cur.execute("SELECT * from states WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()

    for col in rows:
        print(col)
