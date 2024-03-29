#!/usr/bin/python3
""" this module queries database via sql alchemy
    select data from table
"""

from model_state import Base, State
from sys import argv
import sqlalchemy


def select_all():
    """ function to select all data from database """

    con = "mysql://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    engine = sqlalchemy.create_engine(con)
    session = sqlalchemy.orm.sessionmaker(bind=engine)
    Session = session()
    states = Session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    Session.close()


if __name__ == "__main__":
    select_all()
