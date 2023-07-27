#!/usr/bin/python3
"""
Creates a connection to a MySQL database using SQLAlchemy in Python
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    #                                                                      #user      #pass    #db
    engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()
    for data in result:
        print(result)        