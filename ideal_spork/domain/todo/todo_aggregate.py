import json


# Represents a todo item in the database
class Todo:
    # @param id: the id of the todo
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

    # represents sql table for todo collection
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
    def map_for_save(self) -> tuple[str, list]:
        # prepare the statements
        _desc = self.description if self.description is not None else ""
        _is_done = 1 if self.is_done else 0

        # return the sql query and prepared statements
        return (
            "('title', 'description', 'is_done', 'id') VALUES (?,?,?,?)",
            [self.title, _desc, _is_done, self.id],
        )

    # output todo properties to console
    def map_to_json(self):
        return json.dumps(self.__dict__, indent=2)
