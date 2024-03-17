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
    db = MySQLdb.connect(**logininfo)
    db.query("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    output = db.store_result()
    rows = output.fetch_row(maxrows=0)
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    filter()
