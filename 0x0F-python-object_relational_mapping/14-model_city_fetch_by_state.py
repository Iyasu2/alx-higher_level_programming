#!/usr/bin/python3
'''
this module contains code that
lists all states from a
database
'''

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City) \
        .filter(State.id == City.state_id)

    for city in cities:
        print(f"{city.State.name}: ({city.City.id}) {city.City.name}")

    session.close()
