from backend.app.connectors.api_football_connector import ApiFootballConnector


class TeamRepository:

    def __init__(self):
        self.connector = ApiFootballConnector()

    def get(self, team_name: str):
        return self.connector.find_team(team_name)