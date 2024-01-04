# season

from dataclasses import dataclass

from models.team import Team


@dataclass
class Season:
    year: int
    sport: int
    teams: list[Team]
