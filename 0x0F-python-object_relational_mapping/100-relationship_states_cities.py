#!/usr/bin/python3
"""
adds a city "San Francisco" to a database with its
corresponding state "California" using SQLAlchemy.
"""

if __name__ == "__main__":
    from relationship_city import Base, City
    from relationship_state import State
    from sqlalchemy import create_engine, true
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
