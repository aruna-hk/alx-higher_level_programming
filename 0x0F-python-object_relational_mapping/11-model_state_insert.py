#!/usr/bin/python3
""" this module queries database via sql alchemy
    select data from table
"""

from model_state import Base, State
from sys import argv
import sqlalchemy
from sqlalchemy import insert


def select_all_limit():
    """ function to select all data from database """

    con = "mysql://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new = session.query(State).filter_by(name='Louisiana').first()
    print(new.id)
    session.commit()
if __name__ == "__main__":
    select_all_limit()
