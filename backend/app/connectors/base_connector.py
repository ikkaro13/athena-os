from abc import ABC, abstractmethod


class BaseConnector(ABC):

    @abstractmethod
    def get_match(self, league: str, home_team: str, away_team: str):
        """Obtiene la información de un partido."""
        pass

    @abstractmethod
    def get_team(self, team: str):
        """Obtiene información de un equipo."""
        pass

    @abstractmethod
    def get_league(self, league: str):
        """Obtiene información de una liga."""
        pass