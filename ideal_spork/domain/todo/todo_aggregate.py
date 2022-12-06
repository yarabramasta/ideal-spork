import json


# Represents a todo item in the database
class Todo:
    # @param title: the title of the todo
    # @param description: the description of the todo
    # @param is_done: the status of the todo default is False
    def __init__(
        self,
        id: str,
        title: str,
        description: str | None = None,
        is_done: int | bool = False,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.is_done = is_done if isinstance(is_done, bool) else bool(is_done)

        pass

    # sql table for todos
    @staticmethod
    def get_tb() -> str:
        return """
          CREATE TABLE IF NOT EXISTS todos (
            id TEXT PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            description TEXT NULL,
            is_done INTEGER NOT NULL DEFAULT 0
          )
        """

    # map the Todo object to sql statement
    def map_to_sql(self) -> dict:
        # prepare the arguments
        _desc = self.description if self.description is not None else ""
        _is_done = 1 if self.is_done else 0

        # map the arguments into sql statement
        map = {
            "insert": "('title', 'description', 'is_done') VALUES (?,?,?)",
            "update": "SET title = ?, description = ?, is_done = ? WHERE id = ?",
            "data": [self.title, _desc, _is_done],
        }

        return map

    # output todo properties to console
    def map_to_json(self) -> None:
        print(json.dumps(self.__dict__, indent=2))
