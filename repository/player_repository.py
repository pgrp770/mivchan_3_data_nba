from typing import List

from model.player_model import *
from repository.database_repository import get_db_connection


def create_player(player: Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO players(name)
        VALUES (%s) RETURNING ID
        """, (player.name,))
        player_id = cursor.fetchone()["id"]
        connection.commit()
        return player_id


def get_player_by_id(player_id: int) -> Player or None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM players
        WHERE id = %s
        """, (player_id,))
        target_answer = cursor.fetchone()
        if not target_answer:
            return
        return Player(**target_answer)
