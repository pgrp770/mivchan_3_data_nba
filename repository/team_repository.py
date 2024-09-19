from typing import List

from model.team_model import *
from repository.database_repository import get_db_connection


def create_player(team: Team) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO teams(name)
        VALUES (%s) RETURNING ID
        """, (team.name,))
        team_id = cursor.fetchone()["id"]
        connection.commit()
        return team_id


def get_team_by_id(team_id: int) -> Team or None:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        SELECT * FROM teams
        WHERE id = %s
        """, (team_id,))
        target_answer = cursor.fetchone()
        if not target_answer:
            return
        return Team(**target_answer)
