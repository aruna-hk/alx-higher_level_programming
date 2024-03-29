#!/usr/bin/python3
""" this module queries database via sql alchemy
    select data from table
"""

from model_state import Base, State
from sys import argv
import sqlalchemy


def select_all_limit():
    """ function to select all data from database """

    con = "mysql://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = sqlalchemy.create_engine(con)
    session = sqlalchemy.orm.sessionmaker(bind=engine)
    Session = session()
    states = Session.query(State).first()
    if (states is None):
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
    Session.close()


if __name__ == "__main__":
    select_all_limit()
