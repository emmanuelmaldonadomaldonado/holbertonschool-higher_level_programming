#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument in a safe way
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
