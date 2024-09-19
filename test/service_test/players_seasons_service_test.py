from model.player_model import Player
from repository.season_player_repository import *


def test_convert_json_to_player():
    player = {
        "id": 224,
        "playerName": "A.J. Green",
        "position": "SG",
        "age": 23,
        "games": 35,
        "gamesStarted": 1,
        "minutesPg": 345,
        "fieldGoals": 53,
        "fieldAttempts": 125,
        "fieldPercent": 0.424,
        "threeFg": 44,
        "threeAttempts": 105,
        "threePercent": 0.419,
        "twoFg": 9,
        "twoAttempts": 20,
        "twoPercent": 0.45,
        "effectFgPercent": 0.6,
        "ft": 4,
        "ftAttempts": 4,
        "ftPercent": 1,
        "offensiveRb": 6,
        "defensiveRb": 39,
        "totalRb": 45,
        "assists": 22,
        "steals": 6,
        "blocks": 0,
        "turnovers": 9,
        "personalFouls": 31,
        "points": 154,
        "team": "MIL",
        "season": 2023,
        "playerId": "greenaj01"
    }
    from service.players_seasons_service import convert_json_to_player
    res = convert_json_to_player(player)
    assert isinstance(res, Player)


def test_convert_json_to_players_season():
    player = {
        "id": 224,
        "playerName": "A.J. Green",
        "position": "SG",
        "age": 23,
        "games": 35,
        "gamesStarted": 1,
        "minutesPg": 345,
        "fieldGoals": 53,
        "fieldAttempts": 125,
        "fieldPercent": 0.424,
        "threeFg": 44,
        "threeAttempts": 105,
        "threePercent": 0.419,
        "twoFg": 9,
        "twoAttempts": 20,
        "twoPercent": 0.45,
        "effectFgPercent": 0.6,
        "ft": 4,
        "ftAttempts": 4,
        "ftPercent": 1,
        "offensiveRb": 6,
        "defensiveRb": 39,
        "totalRb": 45,
        "assists": 22,
        "steals": 6,
        "blocks": 0,
        "turnovers": 9,
        "personalFouls": 31,
        "points": 154,
        "team": "MIL",
        "season": 2023,
        "playerId": "greenaj01"
    }
    from service.players_seasons_service import convert_json_to_players_season
    result = convert_json_to_players_season(1, player)
    assert isinstance(result, SeasonPlayer)
