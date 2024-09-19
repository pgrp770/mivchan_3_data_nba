from api.api import get_players_for_all_season
from repository.player_repository import get_all_players
from repository.season_player_repository import get_all_season_players
from service.players_seasons_service import insert_players_and_players_seasons


def seed_players_season_players():
    if not get_all_players() and not get_all_season_players():
        json = get_players_for_all_season()
        insert_players_and_players_seasons(json)
