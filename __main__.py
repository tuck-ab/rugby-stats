from .scraper.matchscraper import get_match_data
from .scraper.wcscraper import get_wc_game_links
from .database.tools import add_game, get_connection
from .database.debug import print_database, print_table
from .database.database_setup import reset_database

def run_wc(comp_id):
    links = get_wc_game_links(comp_id)

    for link in links:
        game = get_match_data(link)

        if game:
            conn = get_connection()
            add_game(conn, game)
            conn.close()

if __name__ == "__main__":
    conn = get_connection()
    print_table(conn, "Games")
    