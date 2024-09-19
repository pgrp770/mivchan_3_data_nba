from service.seed_service import seed_players_season_players
from repository.player_repository import get_all_players
from repository.season_player_repository import get_all_season_players


def test_users_seed():
    a = get_all_players()
    b = get_all_season_players()
    assert not a and not b
    seed_players_season_players()
    a = get_all_players()
    b = get_all_season_players()
    assert a and b
