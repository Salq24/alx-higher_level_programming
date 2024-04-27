#!/usr/bin/python3

"""lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Access the database"""
    link_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(link_db)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state_n = session.query(State).filter(State.name.contains('a'))

    if state_n is not None:
        for state in state_n:
            session.delete(state)

    session.commit()

    session.close()
