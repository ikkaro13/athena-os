from backend.app.models.match_context import MatchContext
from backend.app.repositories.team_repository import TeamRepository
from backend.app.repositories.fixture_repository import FixtureRepository
from backend.app.repositories.statistics_repository import StatisticsRepository

class MatchContextService:

    def __init__(self):

        self.team_repository = TeamRepository()

        self.fixture_repository = FixtureRepository()

        self.statistics_repository = StatisticsRepository()

    def build(self, home_team: str, away_team: str):

        home = self.team_repository.get(home_team)
        away = self.team_repository.get(away_team)

        home_fixture = self.fixture_repository.get_last_fixture(home.id)
        away_fixture = self.fixture_repository.get_last_fixture(away.id)

        home_statistics = self.statistics_repository.get_statistics(home_fixture.id)
        away_statistics = self.statistics_repository.get_statistics(away_fixture.id)

        return MatchContext(

            home_team=home,

            away_team=away,

            home_last_fixture=home_fixture,

            away_last_fixture=away_fixture,

            home_statistics=next(
                stat
                for stat in home_statistics
                if stat.team_name == home.name
            ),

            away_statistics=next(
            stat
            for stat in away_statistics
            if stat.team_name == away.name
            )

        )