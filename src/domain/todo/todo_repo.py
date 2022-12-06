from sqlite3 import Connection

from domain.todo.todo_class import Todo


# persistence layer for Todo class
class TodoRepo:
    def __init__(self, client: Connection):
        self.client = client

    def get_all(self) -> list[Todo]:
        # get all todos
        todos = self.client.execute("SELECT * FROM todos")

        # map the todos into Todo object
        return [Todo(*todo) for todo in todos.fetchall()]

    def get_by_id(self, id: int) -> Todo:
        # get todo by id
        todo = self.client.execute("SELECT * FROM todos WHERE id = ?", [id])

        # map the todo into Todo object
        return Todo(*todo.fetchone())

    def create(self, todo: Todo) -> Todo:
        # map the todo object to sql statement
        query = todo.map_to_sql()

        # create todo
        self.client.execute(
            f"INSERT INTO todos {query['insert']}",
            query["data"],
        )

        # get the last inserted id
        todo.id = self.client.execute("SELECT last_insert_rowid()").fetchone()[0]

        return todo

    def update(self, todo: Todo) -> Todo:
        # map the todo object to sql statement
        query = todo.map_to_sql()

        # update todo
        self.client.execute(
            f"UPDATE todos {query['update']}",
            query["data"] + [todo.id],
        )

        return todo

    def delete(self, todo: Todo) -> None:
        # delete todo with id
        self.client.execute("DELETE FROM todos WHERE id = ?", [todo.id])

        pass
