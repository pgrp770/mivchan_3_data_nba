from dataclasses import asdict
from toolz import *

from flask import Blueprint, jsonify, request
from repository.player_repository import *
from repository.season_player_repository import *
from utils.players_controller_utils import filter_players_by_season_and_position

players_blueprint = Blueprint("player", __name__)


@players_blueprint.route("/", methods=["GET"])
def get_all():
    position = request.args.get("position").upper()
    if not position or position not in ["C", "PF", "SF", "SG", "P"]:
        return {"message": "something got wrong with your position"}, 400
    season = request.args.get("season")

    filtered_list = filter_players_by_season_and_position(position, season)

    return jsonify(filtered_list), 200
