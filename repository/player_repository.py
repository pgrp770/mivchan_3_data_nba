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


def create_player_unique(player: Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        check: Player or None = get_id_by_name(player.name)
        if check:
            return check.id

        cursor.execute("""
        INSERT INTO players(name)
        VALUES (%s) RETURNING ID
        """, (player.name,))
        player_id = cursor.fetchone()["id"]
        connection.commit()
        return player_id


def get_id_by_name(name) -> Player or None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM players
        WHERE name = %s
        """, (name,))
        target_answer = cursor.fetchone()
        if not target_answer:
            return
        return Player(**target_answer)


def get_all_players() -> List[Player]:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
           SELECT * FROM players
           """)
        return [Player(**player) for player in cursor.fetchall()]


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
