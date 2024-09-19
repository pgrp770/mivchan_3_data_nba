from flask import Flask

from controller.players_controller import players_blueprint
from repository.database_repository import *
from service.seed_service import seed_players_season_players

app = Flask(__name__)

if __name__ == "__main__":
    # drop_tables_players_and_season_players()
    # create_tables_players_and_season_players()
    # seed_players_season_players()
    app.register_blueprint(players_blueprint, url_prefix="/api/players")
    app.run(debug=True)
