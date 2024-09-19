from dataclasses import dataclass


@dataclass
class SeasonPlayer:
    season_id: int
    team: str
    position: str
    player_id: int
    games: int
    points: int
    twopercent: float
    threepercent: float
    art: float
    id: int = None
