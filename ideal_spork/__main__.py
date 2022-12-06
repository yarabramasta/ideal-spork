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

    choice_msg = "1. Get all todos\n2. Get todo by id\n3. Exit\n\nChoose service: "

    # get user input
    choice = int(input(choice_msg))
    print("")

    while choice != 3:
        # get all todos if user choose 1
        if choice == 1:
            service.get_all()

        # get todo by id if user choose 2
        elif choice == 2:
            service.get_by_id()

        else:
            # invalid choice
            print("Invalid choice!")

        print("=== TODO APP ===")
        choice = int(input(choice_msg))
        print("")

    pass

    client.close()


if __name__ == "__main__":
    main()
