#!/usr/bin/python3
""" login to database and select data """

import sys
from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE


def filter():
    """ filtering output select * from where(filter patter) """

    logininfo = {
        "host": "localhost",
        "user": sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3]
    }
    pattern = '^N'
    db = _mysql.connect(**logininfo)
    db.query("SELECT * FROM states WHERE name REGEXP '%s'" % pattern)
    results = db.store_result()
    filtered = results.fetch_row(maxrows=0)
    for value in filtered:
        print(value)


if __name__ == "__main__":
    filter()
