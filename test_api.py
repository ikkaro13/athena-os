from backend.app.connectors.api_football_connector import ApiFootballConnector

connector = ApiFootballConnector()

league = connector.find_league("Premier League")

print(league)