#!/usr/bin/python3
"""
Establishes a connection to a MySQL database 
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv


    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1], password=argv[2], database=argv[3])
    db = conn.cursor()
    db.execute("SELECT * FROM states;")
    data = db.fetchAll()
    print(data)
    conn.close()
