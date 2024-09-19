from flask import Flask

from repository.database_repository import *

app = Flask(__name__)

if __name__ == "__main__":
    drop_tables_players_and_season_players()
    create_tables_players_and_season_players()
    app.run(debug=True)
