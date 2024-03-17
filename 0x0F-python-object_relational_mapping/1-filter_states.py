#!/usr/bin/python3
""" login to database and select data """

from sys import argv
import MySQLdb


def filter():
    """ filtering output select * from where(filter patter) """

    logininfo = {
        "user": argv[1],
        "password": argv[2],
        "database": argv[3]
    }
    pattern = '^N'
    db = MySQLdb.connect(**logininfo)
    db.query("SELECT * FROM states WHERE name REGEXP '%s'" % pattern)
    results = db.store_result()
    filtered = results.fetch_row(maxrows=0)
    for value in filtered:
        print(value)
    db.close()
if __name__ == "__main__":
    filter()
