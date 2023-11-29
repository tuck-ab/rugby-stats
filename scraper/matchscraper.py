from typing import Optional

import requests
from bs4 import BeautifulSoup

from .rugbyclasses import PlayerSelection, Game, Event
from .static import get_file

def get_match_data(link) -> Optional[Game]:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    page.close()

    report = soup.find("div", {"id": "matchReportCon"})

    ## Getting the teams and score
    box = report.find("div", {"class": "matchReportTitle"})
    home_team = box.find("div", {"class": "titleIntLeft"}).text
    away_team = box.find("div", {"class": "titleIntRight"}).text
    home_score, away_score = box.find("div", {"class": "titleIntCenter"}).text.split("-")

    ## Getting the date
    row = report.find("div", {"id": "matchStats"})
    date = "-".join(row.find("div", {"class": "matchStatsInt"}).text.split(" "))

    ## Getting the squads
    team_lists = report.find_all("ul", {"class": "matchSquads"})
    
    starting_numbers = list(range(15, 8, -1)) + list(range(1, 9))

    home_starts = parse_squad_list(team_lists[0], starting_numbers, home_team)
    away_starts = parse_squad_list(team_lists[1], starting_numbers, away_team)
    home_subs = parse_squad_list(team_lists[2], range(16, 24), home_team)
    away_subs = parse_squad_list(team_lists[3], range(16, 24), away_team)

    players = home_starts + away_starts + home_subs + away_subs

    ## Getting the scoring events
    event_lists = report.find_all("ul", {"class", "matchReportInt"})[1:3]

    ## If the data doesn't exist eg.
    ## https://rugby.statbunker.com/competitions/MatchDetails/World-Cup-2019/Namibia-VS-Canada?comp_id=606&match_id=39756&date=13-Oct-2019
    if len(event_lists) == 0:
        return None

    home_events = parse_event_list(event_lists[0], players)
    away_events = parse_event_list(event_lists[1], players)
    events = home_events + away_events

    game = Game(home_team, away_team, home_score, away_score, date, home_starts,
                away_starts, home_subs, away_subs, events)
    
    return game


def parse_squad_list(ul, numbers, team):
    return [PlayerSelection(li.find("div", {"class": "playerName"}).text, number, team)
            for li, number in zip(ul.find_all("li"), numbers)]


def find_player(name: str, players: list[PlayerSelection], event_type) -> PlayerSelection:
    for player in players:
        if player.name == name:
            return player
    
    print(f"|{event_type}|")
    str_list = "\n".join(map(lambda x: x.name, players))
    raise Exception(f"Player {name} with given name not found in given list \n{str_list}")


def parse_event_list(ul, players: list[PlayerSelection]):
    events = []

    for div in ul.find_all("div", {"class": "matchReportSubInt"}):
        parsed_type = div.small.text.split(", ")
        event_type = parsed_type[0].strip()
        outcome = parsed_type[1] if len(parsed_type) > 1 else None

        if event_type != "pen try":
            name = div.p.text.split(" (")[0]
            player = find_player(name, players, event_type)
            time = div.p.text.split(" (")[1][:-1]
        else:
            player = None
            time = div.p.text.strip()[1:-1]

        events.append(Event(event_type, outcome, player, time))

    return events
