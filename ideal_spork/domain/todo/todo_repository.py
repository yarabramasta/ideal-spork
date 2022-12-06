from sqlite3 import Connection

from .todo_aggregate import Todo


# Persistence layer for Todo using sqlite3
# @param client: the sqlite3 connection
class TodoRepository:
    def __init__(self, client: Connection):
        self.client = client

    def _id(self):
        data = self.client.execute("SELECT id FROM todos")
        # get the last id and increment it by 1
        last_id = data.fetchall()[-1][0]
        return f"{int(last_id) + 1}"

    # get all todos
    def get_all(self):
        data = self.client.execute("SELECT * FROM todos")
        # map the data to Todo object
        return [Todo(*row) for row in data.fetchall()]

    # get todo by id
    # @param id: the id of the todo
    def get_by_id(self, id: str):
        data = self.client.execute("SELECT * FROM todos WHERE id = ?", [id]).fetchone()

        # return None if data is empty
        if data is None:
            return None

        return Todo(*data)

    # save todo to the database
    def create(self, *, title: str, description: str | None = None):
        # instantiate the todo
        todo = Todo(
            id=self._id(),
            title=title,
            description=description,
        )

        # prepare the sql query and statements
        query, statements = todo.map_for_save()

        # execute the query
        self.client.execute(f"INSERT INTO todos {query}", statements)
        self.client.commit()

        # return the todo
        return todo

    def mark_as_done(self, *, id: str):
        # check if todo exists
        todo = self.get_by_id(id)

        if todo is None:
            return None

        # update the todo
        self.client.execute("UPDATE todos SET is_done = 1 WHERE id = ?", [id])
        self.client.commit()

        return Todo(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            is_done=True,
        )

    def delete(self, *, id: str):
        # check if todo exists
        todo = self.get_by_id(id)

        if todo is None:
            return None

        # delete the todo
        self.client.execute("DELETE FROM todos WHERE id = ?", [id])
        self.client.commit()

        return todo
