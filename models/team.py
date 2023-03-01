from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .game import Game

class Base(DeclarativeBase):
    pass

class MLBTeam(Base):
    __tablename__ = "mlb_team"

    mlb_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    teamCode: Mapped[str] = mapped_column(String(5))
    fileCode: Mapped[str] = mapped_column(String(5))
    teamName: Mapped[str] = mapped_column(String(20))
    locationName: Mapped[str] = mapped_column(String(30))
    shortName: Mapped[str] = mapped_column(String(30))
    activePlayers: Mapped[List["Player"]] = relationship()
    seasonGames: Mapped[List["Game"]] = relationship()

    def add_game(self, game: Game):