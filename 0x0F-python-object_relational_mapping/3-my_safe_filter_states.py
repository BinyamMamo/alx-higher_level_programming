#!/usr/bin/python3
"""
Connects to a MySQL database and executes a query to
retrieve data from a table called "states"
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    db = conn.cursor()
    query = """SELECT * FROM states
                        WHERE states.name LIKE BINARY '{}'
                        ORDER BY id;"""
    db.execute(query.format(argv[4]))
    data = db.fetchall()
    for item in data:
        print(item)
    db.close()
    conn.close()