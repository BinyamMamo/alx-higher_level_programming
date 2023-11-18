#!/usr/bin/python3
"""
displays data from a database using mysqldb module
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    con = MySQLdb.connect(host='localhost',
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3])
    cur = con.cursor()

    cur.execute("SELECT * FROM `states` ORDER BY id;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    con.close()
