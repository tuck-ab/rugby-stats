import sqlite3
from sqlite3 import Connection
import pathlib
import os

from ..scraper.rugbyclasses import Game

def get_connection() -> Connection:
    db_dir = os.path.join(pathlib.Path(__file__).parent)
    db_file = os.path.join(db_dir, "data.db")

    conn = sqlite3.connect(db_file)

    return conn



def add_game(conn: Connection, game: Game):
    ## Get team IDs
    home_team_id = get_team_id(conn, game.home_team)
    away_team_id = get_team_id(conn, game.away_team)

    ## Check to see if the game is already in the database
    if game_already_exists(conn, home_team_id, away_team_id, game.date):
        return
    
    ## Add the new game
    cur = conn.cursor()
    new_game_id = cur.execute("SELECT MAX(GameID) FROM Games").fetchall()[0][0] + 1
    cur.execute("INSERT INTO Games VALUES (?, ?, ?, ?, ?, ?)", 
                (new_game_id, home_team_id, away_team_id, game.date,
                 game.home_score, game.away_score))
    conn.commit()
    cur.close()

    ## Add the players
    cur = conn.cursor()
    player_ids = {}

    ## Home players
    for player in game.home_starters + game.home_subs:
        player_id = get_player_id(conn, player.name)
        player_ids[player.name] = player_id

        cur.execute("INSERT INTO PlayerSelections VALUES (?, ?, ?, ?)",
                    (player_id, home_team_id, new_game_id, player.number))
        conn.commit()

    for player in game.away_starters + game.away_subs:
        player_id = get_player_id(conn, player.name)
        player_ids[player.name] = player_id

        cur.execute("INSERT INTO PlayerSelections VALUES (?, ?, ?, ?)",
                    (player_id, away_team_id, new_game_id, player.number))
        conn.commit()

    cur.close()

    ## Add the events
    cur = conn.cursor()
    for event in game.events:
        new_event_id = cur.execute("SELECT MAX(EventID) FROM Events").fetchall()[0][0] + 1
        time = int(event.time.split(" ")[0])
        if event.player:
            player_id = player_ids[event.player.name]
        else:
            player_id = 0
        cur.execute("INSERT INTO Events VALUES (?, ?, ?, ?, ?, ?)",
                    (new_event_id, new_game_id, player_id, event.type, event.outcome, time))
        conn.commit()
    
    cur.close()


def game_already_exists(conn: Connection, ht: int, at: int, date: str) -> bool:
    cur = conn.cursor()
    res = cur.execute(
        """
        SELECT GameID FROM Games
        WHERE HomeTeamID = ? AND AwayTeamID = ? AND Date = ?
        """, 
        (ht, at, date)).fetchall()
    
    if len(res) > 1:
        print("WARNING: Multiple games exist with the same teams on the same date")
        print(f"Home team ID: {ht}")
        print(f"Away team ID: {at}")
        print(f"Game IDs: {', '.join(r[0] for r in res)}\n")

    cur.close()
        
    return len(res) != 0


def get_player_id(conn: Connection, player_name: str) -> int:
    cur = conn.cursor()
    res = cur.execute("SELECT PlayerID FROM Players WHERE Name = ?", (player_name,)).fetchall()
    
    ## There should only be one of each team in the database
    if len(res) > 1:
        raise Exception(f"Multiple players within database have the name {player_name}")
    
    ## If there is one team then return the TeamID
    if len(res) == 1:
        return res[0][0]
    
    ## Otherwise create a new entry for the team
    print(f"Player '{player_name}' not found in Database, creating new entry")

    highest_id = cur.execute("SELECT MAX(PlayerID) FROM Players").fetchall()[0][0]
    cur.execute("INSERT INTO Players VALUES (?, ?)", (highest_id+1, player_name))
    conn.commit()

    cur.close()

    return highest_id + 1


def get_team_id(conn: Connection, team_name: str) -> int:
    cur = conn.cursor()
    res = cur.execute("SELECT TeamID FROM Teams WHERE Name = ?", (team_name,)).fetchall()
    
    ## There should only be one of each team in the database
    if len(res) > 1:
        raise Exception(f"Multiple teams within database have the name {team_name}")
    
    ## If there is one team then return the TeamID
    if len(res) == 1:
        return res[0][0]
    
    ## Otherwise create a new entry for the team
    print(f"Team '{team_name}' not found in Database, creating new entry")

    highest_id = cur.execute("SELECT MAX(TeamID) FROM Teams").fetchall()[0][0]
    cur.execute("INSERT INTO Teams VALUES (?, ?)", (highest_id+1, team_name))
    conn.commit()

    cur.close()

    return highest_id + 1