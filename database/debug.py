from sqlite3 import Connection

def print_database(conn: Connection):
    tables = ["Players", "Teams", "Games", "PlayerSelections", "Events"]
    cur = conn.cursor()

    for table in tables:
        res = cur.execute(f"SELECT * FROM {table}")
        print(f"{table} Table:")
        for item in res:
            print(item)
