#!/usr/bin/python3
""" login to database and select data """

from sys import argv
import MySQLdb


def select_specific():
    """ select specific state """

    logininfo = {
        "host": "localhost",
        "user": argv[1],
        "password": argv[2],
        "database": argv[3]
    }
    db = MySQLdb.connect(**logininfo)
    strt = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    db.query(strt)
    results = db.store_result()
    r = results.fetch_row(maxrows=0)
    for value in r:
        print(value)


if __name__ == "__main__":
    select_specific()
