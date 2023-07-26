#!/usr/bin/python3
import MySQLdb
from sys import argv
username = argv[1]
pwd = argv[2]
dbname = argv[3]
conn = MySQLdb.connect(host='localhost', port=3306, user=username, password=pwd, database=dbname)
db = conn.cursor()
db.execute("SELECT * FROM states;")
data = db.fetchAll()
print(data)
conn.close()