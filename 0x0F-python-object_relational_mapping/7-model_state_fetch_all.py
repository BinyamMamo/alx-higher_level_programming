#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
#                                                                      #user      #pass    #db
engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    Session = sessionMaker(bind=engine)
    session = Session()
    result = session.query(State).all()
    print(result)        