from .todo_repo import TodoRepo


class TodoService:
    def __init__(self, repo: TodoRepo):
        self.repo = repo

    def get_all(self):
        print("=== GET ALL TODOS ===")
        print("Getting all todos from database...")

        todos = self.repo.get_all()

        for todo in todos:
            print(todo.map_to_json(), "\n")
