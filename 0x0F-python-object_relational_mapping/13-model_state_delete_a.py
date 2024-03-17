#!/usr/bin/python3
""" this module queries database via sql alchemy
    select data from table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    con = 'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    engine = create_engine(con)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State).filter(State.name.like('%a%'))
    for instance in objs:
        session.delete(instance)
    session.commit()
