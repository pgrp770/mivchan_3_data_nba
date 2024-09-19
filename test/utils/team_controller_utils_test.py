from utils.team_controller_utils import *


def test_check_5_positions():
    players = [1, 2, 3, 10, 5]
    result1 = check_5_positions(players)
    assert result1
    players2 = [1, 2, 3, 4, 5]
    result2 = check_5_positions(players2)
    assert not result2


def test_create_team_with_players():
    create_team_with_players("asdf", [1, 2, 3, 5, 10])
