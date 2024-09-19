from typing import List

from toolz import *

from model.season_player_model import SeasonPlayer
from repository.season_player_repository import get_all_season_players
from repository.team_player_repository import create_team_player
from repository.team_repository import *


def check_5_positions(list_players_index):
    all_season_players: List[SeasonPlayer] = get_all_season_players()

    players_position = pipe(
        list_players_index,
        partial(map,
                lambda player_id:
                next(filter(lambda player: player.player_id == player_id, all_season_players), None)),
        partial(map, lambda player: player.position if player else None),
        list
    )

    return len(players_position) == len(set(players_position))


def create_team_with_players(team_name, players_id):
    team_id = create_team(Team(team_name))
    for player_id in players_id:
        create_team_player(team_id, player_id)


def update_team_with_players(players_id, team_id):
    for player_id in players_id:
        create_team_player(team_id, player_id)
