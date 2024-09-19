from dataclasses import dataclass


@dataclass
class SeasonPlayer:
    season: int
    team: str
    position: str
    player_id: int
    games: int
    points: int
    twoPercent: float
    threePercent: float
    art: float
    ppg_ratio: float
    id: int = None
