from dataclasses import dataclass

@dataclass
class Fixture:

    id: int
    league: str
    home_team: str
    away_team: str
    date: str
    status: str