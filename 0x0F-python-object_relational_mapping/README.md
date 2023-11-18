# # 0x0F. Python - Object-relational mapping

This project is about using Python to interact with MySQL databases and perform object-relational mapping (ORM) using SQLAlchemy.

<p align="center">
    <img alt="JS sticker" width="100%" src="https://miro.medium.com/v2/resize:fit:640/format:webp/0*3uedj0JV8LWYNc8Q">
</p>

## Introduction

Object-relational mapping is a technique that allows programmers to manipulate data from a database using an object-oriented paradigm. Instead of writing SQL queries, the programmer can use Python classes and methods to create, read, update, and delete data. SQLAlchemy is a popular ORM library for Python that provides a high-level abstraction over MySQL and other databases.

In this project, I used MySQLdb and SQLAlchemy to connect to a MySQL database and execute various operations on the data. I also learned how to map Python classes to MySQL tables and use them to perform ORM.

## Tasks

| Task | Files | Description |
| ---- | ----- | ----------- |
| 0. Get all states | [0-select_states.py](./0-select_states.py) | lists all states from the database `hbtn_0e_0_usa` using MySQLdb |
| 1. Filter states | [1-filter_states.py](./1-filter_states.py) | lists all states with a name starting with `N` from the database `hbtn_0e_0_usa` using MySQLdb |
| 2. Filter states by user input | [2-my_filter_states.py](./2-my_filter_states.py) | takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument using MySQLdb |
| 3. SQL Injection... | [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument, but is safe from MySQL injections using MySQLdb |
| 4. Cities by states | [4-cities_by_state.py](./4-cities_by_state.py) | lists all cities from the database `hbtn_0e_4_usa` using MySQLdb |
| 5. All cities by state | [5-filter_cities.py](./5-filter_cities.py) | takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa` using MySQLdb |
| 6. First state model | [model_state.py](./model_state.py) | contains the class definition of a `State` and an instance `Base = declarative_base()` using SQLAlchemy |
| 7. All states via SQLAlchemy | [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | lists all `State` objects from the database `hbtn_0e_6_usa` using SQLAlchemy |
| 8. First state | [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | prints the first `State` object from the database `hbtn_0e_6_usa` using SQLAlchemy |
| 9. Contains `a` | [9-model_state_filter_a.py](./9-model_state_filter_a.py) | lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa` using SQLAlchemy |
| 10. Get a state | [10-model_state_my_get.py](./10-model_state_my_get.py) | prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa` using SQLAlchemy |


---
<br>
This project has shown me how to use Python to connect to a MySQL database and perform various operations on the data. I have also learned how to use SQLAlchemy to perform object-relational mapping and manipulate data using Python classes and methods. This project has given me a solid foundation for working with databases and ORM in Python.
