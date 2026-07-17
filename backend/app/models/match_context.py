from dataclasses import dataclass

from backend.app.models.team import Team
from backend.app.models.fixture import Fixture
from backend.app.models.statistics import Statistics


@dataclass
class MatchContext:

    home_team: Team
    away_team: Team

    home_last_fixture: Fixture
    away_last_fixture: Fixture

    home_statistics: Statistics
    away_statistics: Statistics