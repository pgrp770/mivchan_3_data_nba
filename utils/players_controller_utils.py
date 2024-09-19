from dataclasses import asdict
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


def get_ppg(player_position):
    all_season_players: List[SeasonPlayer] = list(map(lambda x: asdict(x),get_all_season_players()))
    sum_all_points = pipe(
        all_season_players,
        partial(map, lambda x: x["points"]),
        sum
    )
    return sum_all_points


def filter_players_by_season_and_position(position: str, season: str or None = None) -> List[Player]:
    all_player = get_all_players()
    all_season_players: List[SeasonPlayer] = get_all_season_players()
    season_player_filter = pipe(
        all_season_players,
        partial(filter, lambda player: player.position == position),
        filter_by_season(season),
        partial(map, lambda player: {
            **asdict(player),
            "name": next((p.name for p in all_player if p.id == player.player_id), None),
        }),
        list
    )


    return pipe(
        season_player_filter,
        partial(map, lambda x: {**x, "ppg": x["points"] / get_ppg(x["position"])}),
        list

    )
