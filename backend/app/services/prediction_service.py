from backend.app.connectors.api_football_connector import ApiFootballConnector


class PredictionService:

    def __init__(self):
        self.connector = ApiFootballConnector()

    def predict(self, league, home_team, away_team):

        match_data = self.connector.get_match(
            league,
            home_team,
            away_team
        )

        print(">>> PredictionService ejecutándose <<<")
        print(match_data)

        winner = home_team
        probability = 50.0
        confidence = "Low"
        reason = "Default prediction."

        if home_team == "Liverpool":
            winner = "Liverpool"
            probability = 72.5
            confidence = "High"
            reason = "Strong home performance."

        elif home_team == "Manchester City":
            winner = "Manchester City"
            probability = 78.3
            confidence = "High"
            reason = "Excellent recent statistics."

        elif away_team == "Real Madrid":
            winner = "Real Madrid"
            probability = 69.8
            confidence = "High"
            reason = "Historical away performance."

        return {
            "league": league,
            "winner": winner,
            "probability": probability,
            "confidence": confidence,
            "reason": reason
        }