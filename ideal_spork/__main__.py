### code by yarabramasta<yarabram111@gmail.com> ###

from .data.db import db_conn, migration
from .domain.todo import TodoRepo, TodoService


def main():
    # Setup database connection and migration with seedings
    client = db_conn()
    migration(client, with_seed=True)

    print("=== TODO APP ===")

    # initialize services
    service = TodoService(TodoRepo(client))

    # get user input
    choice = int(input("1. Get all todos\n2. Exit\n\nChoose service: "))
    print("")

    while choice != 2:
        if choice == 1:
            service.get_all()
        else:
            print("Invalid choice!")

        print("=== TODO APP ===")
        choice = int(input("1. Get all todos\n2. Exit\n\nChoose service: "))
        print("")

    pass


if __name__ == "__main__":
    main()
