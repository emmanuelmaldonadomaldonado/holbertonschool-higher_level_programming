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
    
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        # Si se encontró el objeto, imprimir su id
        print(state.id)
    else:
        # Si no se encontró el objeto, imprimir "Not found"
        print("Not found")
    
    session.close()
