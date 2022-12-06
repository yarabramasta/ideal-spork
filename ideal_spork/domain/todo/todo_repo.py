from sqlite3 import Connection

from .todo_aggregate import Todo


# Persistence layer for Todo using sqlite3
# @param client: the sqlite3 connection
class TodoRepo:
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

        print("fetching")
        print(data)
