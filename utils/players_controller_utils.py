from typing import List

from toolz import *

from model.player_model import Player
from model.season_player_model import SeasonPlayer
from repository.player_repository import get_all_players
from repository.season_player_repository import get_all_season_players


@curry
def filter_by_season(season, li):
    if season:
        return pipe(
            li,
            partial(filter, lambda player: player.season_id == int(season)),
            list
        )
    return li


def filter_players_by_season_and_position(position: str, season: str or None = None) -> List[Player]:
    all_player = get_all_players()
    all_season_players: List[SeasonPlayer] = get_all_season_players()
    season_player_filter = pipe(
        all_season_players,
        partial(filter, lambda player: player.position == position),
        filter_by_season(season),
        partial(map, lambda player: player.player_id),
        set,
        list
    )
    filter_player = pipe(
        all_player,
        partial(filter, lambda player: player.id in season_player_filter),
        list
    )
    return filter_player

