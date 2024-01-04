# games



@dataclass
class Game:
	id: str
	date: str
	home_team: Team
	away_team: Team
	home_score: int
	away_score: int
	location: str
