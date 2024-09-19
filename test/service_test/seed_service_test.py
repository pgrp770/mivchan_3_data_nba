from service.seed_service import users_seed
from repository.player_repository import get_all_players
from repository.season_player_repository import get_all_season_players


def test_users_seed():
    a = get_all_players()
    b = get_all_season_players()
    assert not a and not b
    users_seed()
    a = get_all_players()
    b = get_all_season_players()
    assert a and b
