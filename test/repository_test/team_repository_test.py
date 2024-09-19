import pytest

from repository.team_repository import *
from repository.database_repository import *


@pytest.fixture(scope='module')
def setup_database():
    create_teams_table()
    yield

    conn = get_db_connection()
    cur = conn.cursor()
    # drop_all_tables()
    conn.commit()
    cur.close()
    conn.close()


def test_create_answer():
    new_player = Team("test")
    new_id = create_player(new_player)
    assert get_team_by_id(new_id).id == new_id
