from dataclasses import dataclass
from enum import Enum
from typing import Optional

@dataclass
class PlayerSelection:
    name: str
    number: int
    team: str

    def __str__(self) -> str:
        return f"{self.team} ({self.number}): {self.name}"
    
    def game_str(self) -> str:
        return f"{self.number} {self.name}"

@dataclass
class Event:
    type: str
    outcome: Optional[str]
    player: Optional[PlayerSelection]
    time: str
    
@dataclass
class Game:
    home_team: str
    away_team: str
    home_score: int
    away_score: int
    date: str
    home_starters: list[PlayerSelection]
    away_starters: list[PlayerSelection]
    home_subs: list[PlayerSelection]
    away_subs: list[PlayerSelection]
    events: list[Event]

    def get_players(self) -> list[PlayerSelection]:
        return self.home_starters + self.away_starters + self.home_subs + self.away_subs

    def __str__(self) -> str:
        out_str = ""
        out_str += f"\t {'Home': <20} \t {'Away': <20}\n\n"
        out_str += f"\t {f'{self.home_team} - {self.home_score}': <20} \t"
        out_str += f" {f'{self.away_team} - {self.away_score}': <20}\n"

        out_str += f"Teams:\n"
        for hn, an in zip(self.home_starters, self.away_starters):
            out_str += f"\t {hn.game_str(): <20} \t {an.game_str(): <20}\n"

        out_str += f"Bench:\n"
        for hn, an in zip(self.home_subs, self.away_subs):
            out_str += f"\t {hn.game_str(): <20} \t {an.game_str(): <20}\n"

        out_str += f"Events:\n"
        for event in sorted(self.events, key=lambda x: int(x.time.split(" ")[0])):
            out_str += f"\t {event.time: <7}: {event.type: <4} from {event.player.name: <20} {event.outcome}\n"

        return out_str
