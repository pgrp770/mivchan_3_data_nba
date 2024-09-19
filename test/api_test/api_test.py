from api.api import *


def test_get_players_by_season():
    result = get_players_by_season(2022)
    assert len(result) >= 0


def test_get_players_for_all_season():
    result = get_players_for_all_season()
    assert len(result) >= 0
