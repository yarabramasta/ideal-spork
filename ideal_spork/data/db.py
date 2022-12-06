# Description: Module for database connection and migration

from os import path
from sqlite3 import Connection, connect

from ..domain.todo import Todo


# open the sqlite database connection
def db_conn() -> Connection:
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
def migration(client: Connection, *, with_seed: bool = False) -> None:

    # create table and seed data if its empty
    client.execute(Todo.get_tb())
    client.commit()

    seed(client) if with_seed else None


# seed the database
def seed(client: Connection) -> None:

    # get all todos
    existing = client.execute("SELECT * FROM todos")

    # seed data
    mock_todos = [
        Todo("1101", "Learn Python", "Learn Python from scratch", True),
        Todo("1102", "Learn SQL", "Learn SQL from scratch"),
    ]

    # check if todos is empty
    if len(existing.fetchall()) == 0:
        print("Seeding data...")
        # insert todos
        for todo in mock_todos:
            # map the todo object to sql statement
            query = todo.map_for_save()

            # create seed data
            client.execute(
                f"INSERT INTO todos {query['insert']}",
                query["data"],
            )

        print("Seeding data done!")

    client.commit()
