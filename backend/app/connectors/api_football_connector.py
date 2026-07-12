from backend.app.connectors.base_connector import BaseConnector
from backend.app.core.http_client import HttpClient
from backend.config import settings
from backend.app.models.team import Team


class ApiFootballConnector(BaseConnector):

    def __init__(self):
        self.client = HttpClient()

    def get_match(self, league: str, home_team: str, away_team: str):
        pass

    def get_team(self, team: str):

        url = f"{settings.API_FOOTBALL_URL}/teams"

        headers = {
            "x-apisports-key": settings.API_FOOTBALL_KEY
        }

        params = {
            "search": team
        }

        return self.client.get(
            url=url,
            headers=headers,
            params=params
        )

    def get_league(self, league: str):

        url = f"{settings.API_FOOTBALL_URL}/leagues"

        headers = {
            "x-apisports-key": settings.API_FOOTBALL_KEY
        }

        return self.client.get(
            url=url,
            headers=headers
        )

    def find_league(self, league_name: str):

        response = self.get_league(league_name)

        if not response:
            return None

        for item in response["response"]:

            league = item["league"]

            if league["name"].lower() == league_name.lower():

                return {
                    "id": league["id"],
                    "name": league["name"],
                    "country": item["country"]["name"],
                    "type": league["type"]
                }
            
    def find_team(self, team_name: str):

        response = self.get_team(team_name)

        if not response:
            return None

        if response["results"] == 0:
            return None

        team = response["response"][0]["team"]

        return Team(
            id=team["id"],
            name=team["name"],
            country=team["country"],
            code=team["code"]
        )