from .todo_repo import TodoRepo


# Access layer for Todo business logic inside domain
# @param repo: the TodoRepo instance
class TodoService:
    def __init__(self, repo: TodoRepo):
        self.repo = repo

    def get_all(self):
        print("=== GET ALL TODOS ===")
        print("\nGetting all todos from database...\n")

        todos = self.repo.get_all()

        print("\nMy Todos:") if len(todos) > 0 else print("\nNo todos found!")
        print("")

        if len(todos) == 0:
            return

        # output the todos to console in json format
        for todo in todos:
            print(todo.map_to_json())
        print("")

    def get_by_id(self):
        print("=== GET TODO BY ID ===")
        # @param id: the id of the todo
        id = input("Enter todo id: ")

        print(f"\nGetting todo with id {id} from database...\n")

        todo = self.repo.get_by_id(id)

        if todo is None:
            print("\nTodo not found!")
            print("")
            return

        # output the todo to console in json format if todo is not None
        print(todo.map_to_json(), "\n")

    def save(self):
        print("=== CREATE NEW TODO ===")

        # @param title: the title of the todo
        title = input("Enter todo title: ")
        # @param description: the description of the todo
        description = input("Enter todo description: ")

        print(f"\nSaving todo with title {title} to database...\n")

        todo = self.repo.create(title=title, description=description)

        print("\nTodo saved!\n")
        print(todo.map_to_json(), "\n")

    def mark_as_done(self):
        print("=== MARK TODO AS DONE ===")
        # @param id: the id of the todo
        id = input("Enter todo id: ")

        print(f"\nMarking todo with id {id} as done...\n")

        todo = self.repo.mark_as_done(id=id)

        if todo is None:
            print("\nTodo not found!")
            print("")
            return

        print("\nTodo marked as done!\n")
        print(todo.map_to_json(), "\n")

    def delete(self):
        print("=== DELETE TODO ===")
        # @param id: the id of the todo
        id = input("Enter todo id: ")

        print(f"\nDeleting todo with id {id} from database...\n")

        todo = self.repo.delete(id=id)

        if todo is None:
            print("\nTodo not found!")
            print("")
            return

        print("\nTodo deleted!\n")
        print(todo.map_to_json(), "\n")
