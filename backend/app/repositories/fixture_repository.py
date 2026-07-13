from backend.app.connectors.api_football_connector import ApiFootballConnector
from backend.app.models.fixture import Fixture


class FixtureRepository:

    def __init__(self):
        self.connector = ApiFootballConnector()

    def get_last_fixture(self, team_id: int):

        response = self.connector.get_fixtures(team_id)

        if not response:
            return None

        if response["results"] == 0:
            return None

        item = response["response"][0]

        return Fixture(
            id=item["fixture"]["id"],
            league=item["league"]["name"],
            home_team=item["teams"]["home"]["name"],
            away_team=item["teams"]["away"]["name"],
            date=item["fixture"]["date"],
            status=item["fixture"]["status"]["long"]
        )