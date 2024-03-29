#!/usr/bin/python3
"""
Establishes a connection to a MySQL database and
retrieves data from a table called `State`
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:
                           3306/{}""".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    data = session.query(State).order_by(State.id).all()
    for d in data:
        print(d.id, ": ", d.name, sep="")
