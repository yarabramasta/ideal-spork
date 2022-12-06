from sqlite3 import Connection

from .todo_aggregate import Todo


class TodoRepo:
    def __init__(self, client: Connection):
        self.client = client

    def _id(self):
        data = self.client.execute("SELECT id FROM todos")
        last_id = data.fetchall()[-1][0]
        return f"{int(last_id) + 1}"

    def get_all(self):
        data = self.client.execute("SELECT * FROM todos")
        return [Todo(*row) for row in data.fetchall()]
