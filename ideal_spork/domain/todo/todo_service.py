from .todo_repo import TodoRepo


# Access layer for Todo business logic inside domain
# @param repo: the TodoRepo instance
class TodoService:
    def __init__(self, repo: TodoRepo):
        self.repo = repo

    def get_all(self):
        print("=== GET ALL TODOS ===")
        print("Getting all todos from database...")

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

        id = input("Enter todo id: ")

        print(f"Getting todo with id {id} from database...")

        todo = self.repo.get_by_id(id)

        if todo is None:
            print("\nTodo not found!")
            print("")
            return

        # output the todo to console in json format if todo is not None
        print(todo.map_to_json(), "\n")
