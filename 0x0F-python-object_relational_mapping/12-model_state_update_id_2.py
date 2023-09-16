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

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    rename_state = session.query(State) \
        .filter(State.id == 2).first()
    rename_state.name = 'New Mexico'
    session.commit()

    session.close()
