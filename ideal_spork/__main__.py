### code by yarabramasta<yarabram111@gmail.com> ###

from .data.db import db_conn, migration
from .domain.todo import TodoRepository, TodoService


def main():
    # Setup database connection and migration with seedings
    client = db_conn()
    migration(client, with_seed=True)

    print("=== TODO APP ===")

    # initialize services
    service = TodoService(TodoRepository(client))

    choice_msg = "1. Get all todos\n2. Get todo by id\n3. Add new todo\n4. Mark todo as done\n5. Delete todo\n6. Exit\n\nChoose service: "

    # get user input
    choice = int(input(choice_msg))
    print("")

    while choice != len(choice_msg.split(".")) - 1:
        # get all todos if user choose 1
        if choice == 1:
            service.get_all()

        # get todo by id if user choose 2
        elif choice == 2:
            service.get_by_id()

        # create todo
        elif choice == 3:
            service.save()

        # update todo.is_done to True
        elif choice == 4:
            service.mark_as_done()

        # delete todo
        elif choice == 5:
            service.delete()

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
