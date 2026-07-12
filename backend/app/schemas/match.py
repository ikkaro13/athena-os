from pydantic import BaseModel


class MatchRequest(BaseModel):
    league: str
    home_team: str
    away_team: str