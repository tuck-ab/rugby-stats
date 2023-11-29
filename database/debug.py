from sqlite3 import Connection

def print_database(conn: Connection):
    tables = ["Players", "Teams", "Games", "PlayerSelections", "Events"]
    for table in tables:
        print_table(conn, table)

def print_table(conn: Connection, table: str):
    cur = conn.cursor()
    res = cur.execute(f"SELECT * FROM {table}")
    print(f"{table} Table:")
    for item in res:
        print(item)
    cur.close()
