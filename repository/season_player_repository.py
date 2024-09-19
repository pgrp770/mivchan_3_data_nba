from typing import List

from model.season_player_model import *
from repository.database_repository import get_db_connection


def create_player_season(season_player: SeasonPlayer) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO season_players(
               season_id,
               player_id,
               team,
               position,
               games,
               points,
               twoPercent,
               threePercent,
               art)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING ID
        """, (
            season_player.season_id,
            season_player.player_id,
            season_player.team,
            season_player.position,
            season_player.games,
            season_player.points,
            season_player.twopercent,
            season_player.threepercent,
            season_player.art
        ))
        player_id = cursor.fetchone()["id"]
        connection.commit()
        return player_id


def get_player_season_by_id(season_players_id: int) -> SeasonPlayer or None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM season_players
        WHERE id = %s
        """, (season_players_id,))
        target_answer = cursor.fetchone()
        if not target_answer:
            return
        return SeasonPlayer(**target_answer)
