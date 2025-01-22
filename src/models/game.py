# games
from src.models.base import Base
from src.models.team import Team


class Game(Base):
    id: str
    date: str
    home_team: Team
    away_team: Team
    home_score: int
    away_score: int
    location: str
