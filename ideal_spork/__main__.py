### code by yarabramasta<yarabram111@gmail.com> ###

from .data.db import db_conn, migration


def main():
    client = db_conn()

    client.execute("DROP TABLE IF EXISTS todos")
    migration(client, with_seed=True)

    pass


if __name__ == "__main__":
    main()
