from typing import List

from toolz import get_in

from model.player_model import *
from model.season_player_model import *
from repository.player_repository import *
from repository.season_player_repository import *


def calculate_art(assists: int, turnover: float) -> float:
    if turnover == 0:
        return 0
    return assists / turnover


def calculate_points(two_points: int, three_points: int) -> int:
    return two_points * 2 + three_points * 3


def convert_json_to_player(json: dict) -> Player:
    player_name = get_in(["playerName"], json)

    return Player(player_name)


def convert_json_to_players_season(player_id: int, json) -> SeasonPlayer:
    season_id = get_in(["season"], json)
    team = get_in(["team"], json)
    position = get_in(["position"], json)
    player_id = player_id
    games = get_in(["games"], json)
    points = calculate_points(json["twoFg"], json["threeFg"])
    twopercent = get_in(["twoPercent"], json)
    threepercent = get_in(["threePercent"], json)
    art = calculate_art(json["assists"], json["turnovers"])
    return SeasonPlayer(
        season_id,
        team,
        position,
        player_id,
        games,
        points,
        twopercent,
        threepercent,
        art
    )


def insert_players_and_players_seasons(json: List[dict]):
    for player_json in json:
        player = convert_json_to_player(player_json)
        player_id = create_player_unique(player)
        season_player = convert_json_to_players_season(player_id, player_json)
        create_player_season(season_player)

