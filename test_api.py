from backend.app.connectors.api_football_connector import ApiFootballConnector

connector = ApiFootballConnector()

team = connector.find_team("Liverpool")

print(team)