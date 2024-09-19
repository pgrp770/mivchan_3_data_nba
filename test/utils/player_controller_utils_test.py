from model.player_model import Player
from utils.players_controller_utils import *


def test_filter_players_by_season_and_position():
    result = filter_players_by_season_and_position("PF", 2022)
    assert all(isinstance(player, dict) for player in result)


def test_get_ppg():
    a = get_ppg("PF")
    assert True
