#!/usr/bin/python3
"""
Establishes a connection to a MySQL database using the provided
command line arguments and fetches the first row of the States stable
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
    data = session.query(State).order_by(State.id).filter(State.name.like("%a%")).all()
    print(*[f"{d.id}: {d.name}" for d in data], sep="\n")
