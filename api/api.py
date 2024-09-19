import requests


def get_players_by_season(year: int) -> list:
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/season/{year}"
    response = requests.get(url)
    return response.json()


def get_players_for_all_season() -> list:
    all_players = []
    for year in [2022, 2023, 2024]:
        all_players += get_players_by_season(year)
    return all_players
