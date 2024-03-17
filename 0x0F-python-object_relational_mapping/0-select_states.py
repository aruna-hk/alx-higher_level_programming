#!/usr/bin/python3

""" this module contains script for connection to mysql server using
    mysqldb connector, and using the connection to query database
    ./thisscript mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

connectioninfo = {
    "port": 3306,
    "user": argv[1],
    "password": argv[2],
    "db": argv[3]
}
query = "select * from states order by id ASC"
connection = MySQLdb.connect(**connectioninfo)
connection.query(query)
result = connection.store_result()
selected = result.fetch_row(maxrows=0)
for row in selected:
    print(row)
connection.close()
