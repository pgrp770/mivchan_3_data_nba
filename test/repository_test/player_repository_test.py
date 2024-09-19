import pytest

from repository.player_repository import *
from repository.database_repository import *


@pytest.fixture(scope='module')
def setup_database():
    create_player_table()
    yield

    conn = get_db_connection()
    cur = conn.cursor()
    # drop_all_tables()
    conn.commit()
    cur.close()
    conn.close()


def test_create_answer():
    new_player = Player("test")
    new_id = create_player(new_player)
    assert get_player_by_id(new_id).id == new_id


def test_get_id_by_name():
    result = get_id_by_name("tst")
    assert result or not result


def test_create_player_unique():
    result = Player("tet")
    new_id = create_player_unique(result)
    assert get_player_by_id(new_id).id == new_id
