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


def test_create_team():
    new_team = Team("test")
    new_id = create_team(new_team)
    assert get_team_by_id(new_id).id == new_id


def test_delete_team():
    result = delete_team(1)
    check_user_answer = get_team_by_id(1)
    assert not check_user_answer
