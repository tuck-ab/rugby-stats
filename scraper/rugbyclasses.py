from dataclasses import dataclass
from enum import Enum

@dataclass
class PlayerSelection:
    name: str
    number: int
    team: str

    def __repr__(self):
        return f"{self.team} ({self.number}): {self.name}"

@dataclass
class Event:
    type: str
    outcome: str
    player: str
    time: str
    
@dataclass
class Game:
    home_team: str
    away_team: str
    home_score: int
    away_score: int
    home_starters: [PlayerSelection]
    away_starters: [PlayerSelection]
    home_subs: [PlayerSelection]
    away_subs: [PlayerSelection]
    events: [Event]
