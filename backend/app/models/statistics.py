from dataclasses import dataclass


@dataclass
class Statistics:

    team_name: str
    possession: float
    shots: int
    shots_on_goal: int
    corners: int
    fouls: int