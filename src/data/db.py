# Description: Module for database connection and migration

from os import path
from sqlite3 import Connection, connect

from domain.todo.todo_class import Todo


# open the sqlite database connection
def db() -> Connection:
    # empty variable for sqlite3.Connection
    client = None

    # check if the sqlite.db file exists
    if not path.isfile("sqlite.db"):
        # write the sqlite.db file
        open("sqlite.db", "w").close()

    # connect to the sqlite.db file
    client = connect("sqlite.db")

    # return the client
    return client


# run database migration
def migration() -> None:
    client = db()

    # create table and seed data if its empty
    client.execute(Todo.get_tb())
    seed()

    client.close()


# seed the database
def seed() -> None:
    client = db()

    # get all todos
    existing = client.execute("SELECT * FROM todos")

    # seed data
    mock_todos = [
        Todo("Learn Python", "Learn Python from scratch", True),
        Todo("Learn SQL", "Learn SQL from scratch"),
    ]

    # check if todos is empty
    if len(existing.fetchall()) == 0:
        # insert todos
        for todo in mock_todos:
            # map the todo object to sql statement
            query = todo.map_to_sql()

            # create seed data
            client.execute(
                f"INSERT INTO todos {query['insert']}",
                query["data"],
            )

    client.close()
