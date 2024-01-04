from abc import ABC, abstractmethod

from .game import Game
from .player import Player
from .season import Season
from .exceptions import StringValidatorError
from .base import validate_string


class Team(ABC):
    @abstractmethod
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def set_name(self, name: str):
        if validate_string(name):
            self._name = name
        else:
            raise StringValidatorError("Invalid value for 'name' provided.")

    @abstractmethod
    @property
    def team_code(self):
        return self._team_code
    
    @abstractmethod
    def set_team_code(self, code: str):
        if validate_string(code):
            self._team_code = code
        else:
            raise StringValidatorError("Invalid value for 'team_code' provided.")


class MLBTeam(Team):

    _name: str
    _team_code: str
    mlb_id: int
    file_code: str
    team_name: str
    location_name: str
    short_name: str
    active_players: list[Player]
    current_season: Season

    def add_game(self, game: Game):