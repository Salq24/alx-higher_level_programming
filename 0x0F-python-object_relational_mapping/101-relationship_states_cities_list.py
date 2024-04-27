#!/usr/bin/python3

"""lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    """Access the database"""
    link_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)

    engine = create_engine(link_db)

    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    n_state = session.query(State).outerjoin(City)\
        .order_by(State.id, City.id).all()

    for state in n_state:
        print(f"{state.id}: {state.name}")

        for cty in state.cities:
            print(f"    {city.id}: {city.name}")
