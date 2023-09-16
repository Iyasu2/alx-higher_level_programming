#!/usr/bin/python3
'''
this module contains code that
lists all states from a
database
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]))
Base = declarative_base()

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
