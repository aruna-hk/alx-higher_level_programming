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
    db = MySQLdb.connect(**logininfo)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (argv[4],))
    rows = cursor.fetchall()
    objs = list(row[0] for row in rows)
    print(*objs, sep=", ")
    cursor.close()
    db.close()


if __name__ == "__main__":
    select_join()
