CHECK_TEAM_SQL = """
    SELECT * FROM Teams
    WHERE Name = ?;
"""

GET_HIGHEST_ID = """
    SELECT MAX({id}) FROM {table};
"""

ADD_PLAYER = """
    INSERT INTO Players VALUES
    (?, ?);
"""

ADD_TEAM = """
    INSERT INTO Teams VALUES
    (?, ?);
"""

ADD_GAME = """
    INSERT INTO Games VALUES
    (?, ?, ?, ?, ?, ?);
"""

ADD_PLAYER_SELECTION = """
    INSERT INTO PlayerSelections VALUES
    (?, ?, ?, ?);
"""

ADD_EVENT = """
    INSERT INTO Events VALUES
    (?, ?, ?, ?, ?, ?);
"""
