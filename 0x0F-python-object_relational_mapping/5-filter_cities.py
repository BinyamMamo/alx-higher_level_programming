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
    db.execute("""SELECT
                        c.name
                    FROM cities c
                    JOIN states s
                        ON c.state_id = s.id
                    WHERE s.name = '{}'
                    ORDER BY c.id;""".format(argv[4]))
    data = db.fetchall()
    print(", ".join([item[0] for item in data]))
    db.close()
    conn.close()
