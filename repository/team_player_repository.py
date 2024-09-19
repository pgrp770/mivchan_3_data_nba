from typing import List


from repository.database_repository import get_db_connection


def create_team_player(team_id, player_id) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO player_teams(player_id, team_id)
        VALUES (%s, %s) RETURNING ID
        """, (player_id, team_id))
        team_player_id = cursor.fetchone()["id"]
        connection.commit()
        return team_player_id


