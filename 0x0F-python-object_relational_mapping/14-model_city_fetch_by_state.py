#!/usr/bin/python3
"""
creates a session to a MySQL database and queries all the cities
in the database, ordered by their ID; then prints the name of
the state, ID, and name of each city.
"""

if __name__ == "__main__":
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:3306
                           /{}""".format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()

    data = session.query(City).join(State).order_by(City.id).all()
    for d in data:
        print(d.state.name, ": (", d.id, ") ", d.name, sep="")
