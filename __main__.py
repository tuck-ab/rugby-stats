from .scraper.matchscraper import get_match_data
from .database.tools import add_game, get_connection
from .database.debug import print_database
from .database.database_setup import reset_database

if __name__ == "__main__":
    ## Parse the game using the scraper
    game = get_match_data("https://rugby.statbunker.com/competitions/MatchDetails/World-Cup-2019/England-VS-South-Africa?comp_id=606&match_id=40373&date=02-Nov-2019")

    reset_database()

    ## Add the game information to the DB
    conn = get_connection()
    add_game(conn, game)

    print_database(conn)

    conn.close()
    