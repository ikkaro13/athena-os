from backend.app.connectors.api_football_connector import ApiFootballConnector
from backend.app.models.statistics import Statistics


class StatisticsRepository:

    def __init__(self):
        self.connector = ApiFootballConnector()

    def get_statistics(self, fixture_id: int):

        response = self.connector.get_statistics(fixture_id)

        if not response:
            return []

        if response.get("results", 0) == 0:
            return []

        statistics = []

        for item in response["response"]:

            stats = {}

            for stat in item["statistics"]:
                stats[stat["type"]] = stat["value"]

            statistics.append(

                Statistics(

                    team_name=item["team"]["name"],

                    possession=float(
                        str(stats.get("Ball Possession", "0")).replace("%", "")
                    ),

                    shots=int(stats.get("Total Shots", 0)),

                    shots_on_goal=int(
                        stats.get("Shots on Goal", 0)
                    ),

                    corners=int(
                        stats.get("Corner Kicks", 0)
                    ),

                    fouls=int(
                        stats.get("Fouls", 0)
                    )

                )

            )

        return statistics