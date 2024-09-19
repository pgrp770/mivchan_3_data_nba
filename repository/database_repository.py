import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI, cursor_factory=RealDictCursor)


def create_player_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        )   
        """)
        connection.commit()


def create_teams_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        )   
        """)
        connection.commit()


def create_player_team_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_teams (
            id SERIAL PRIMARY KEY,
            player_id INT NOT NULL,
            team_id INT NOT NULL,
            FOREIGN KEY(player_id) REFERENCES players(id) ON DELETE CASCADE,
            FOREIGN KEY(team_id) REFERENCES teams(id) ON DELETE CASCADE
        )   
        """)
        connection.commit()


def create_season_player_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
           CREATE TABLE IF NOT EXISTS season_players (
               id SERIAL PRIMARY KEY,
               season_id INT NOT NULL,
               player_id INT NOT NULL,
               team VARCHAR(100) NOT NULL,
               position VARCHAR(100) NOT NULL,
               games INT NOT NULL,
               points INT NOT NULL,
               twoPercent REAL,
               threePercent REAL,
               art REAL NOT NULL,
               FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
           )   
           """)
        connection.commit()


def create_tables_players_and_season_players():
    create_player_table()
    create_season_player_table()


def create_tables_team_and_player_team():
    create_teams_table()
    create_player_team_table()


def drop_tables_players_and_season_players():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            DROP TABLE IF EXISTS season_players;
            DROP TABLE IF EXISTS players;
        ''')


def drop_tables_team_and_player_team():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
            DROP TABLE IF EXISTS player_teams;
            DROP TABLE IF EXISTS teams;
        ''')
