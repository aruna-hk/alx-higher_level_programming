#!/usr/bin/python3
""" login to database and select data """

from sys import argv
import re
import MySQLdb


def select_specific():
    """ select specific state """

    pattern = r'[^a-zA-Z0-9_]'
    clean = re.sub(pattern, ' ', argv[4])
    state = clean.split(' ')[0]
    logininfo = {
        "host": "localhost",
        "user": argv[1],
        "password": argv[2],
        "database": argv[3]
    }
    db = MySQLdb.connect(**logininfo)
    strt = "select * from states where name = '{}' order by id".format(state)
    db.query(strt)
    results = db.store_result()
    r = results.fetch_row(maxrows=0)
    for value in r:
        print(value)


if __name__ == "__main__":
    select_specific()
