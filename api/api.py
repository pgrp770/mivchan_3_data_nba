import requests


def get_players_by_season(year: int) -> list:
    url = f"https://nba-stats-db.herokuapp.com/api/playerdata/season/{year}/"
    response = requests.get(url)
    return response.json()["results"]


def get_players_for_all_season() -> list:
    all_players = []
    for year in [2022, 2023, 2024]:
        all_players += get_players_by_season(year)
    return all_players
