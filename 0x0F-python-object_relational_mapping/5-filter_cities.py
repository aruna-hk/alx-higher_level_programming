#!/usr/bin/python3
""" select module select cities and join with states
   user inner join to place a city in its state
   select * cities inner join states on ids
"""
import MySQLdb
from sys import argv


def select_join():
    """ function to execute select and join when called """

    logininfo = {
        "user": argv[1],
        "password": argv[2],
        "db": argv[3]
    }
    query = """select cities.name from cities inner join states
        where states.name = "{}"
        """.format(argv[4])
    db = MySQLdb.connect(**logininfo)
    db.query(query)
    result = db.store_result()
    fetch = result.fetch_row(maxrows=0)
    lenn = len(fetch)
    i = 0
    for value in fetch:
        print(value[0], end='')
        if (i < lenn - 1):
            print(", ", end='')
        i = i + 1
    print()


if __name__ == "__main__":
    select_join()
