from dataclasses import asdict
from toolz import *

from flask import Blueprint, jsonify, request
from repository.player_repository import *
from repository.season_player_repository import *
from repository.team_repository import delete_team
from utils.players_controller_utils import filter_players_by_season_and_position
from utils.team_controller_utils import *

teams_blueprint = Blueprint("team", __name__)


@teams_blueprint.route("/", methods=["POST"])
def create_team():
    new_team = request.json
    players_id = new_team["players_id"]
    if len(players_id) != 5:
        return jsonify({"message": "you need to give 5 id's "}), 400
    if not check_5_positions(players_id):
        return jsonify({"message": "you need to have player for each position"}, 400)
    team_name = new_team["team_name"]
    create_team_with_players(team_name, players_id)
    return jsonify({}), 200


@teams_blueprint.route("/<int:team_id>", methods=["PUT"])
def update_team(team_id):
    new_team = request.json
    players_id = new_team["players_id"]
    if len(players_id) != 5:
        return jsonify({"message": "you need to give 5 id's "}), 400
    if not check_5_positions(players_id):
        return jsonify({"message": "you need to have player for each position"}, 400)
    team_name = new_team["team_name"]
    a = get_team_by_id(team_id)
    delete_team(team_id)
    create_team_with_id(Team(a.name, team_id))
    update_team_with_players(players_id, team_id)
    return jsonify({}), 200


@teams_blueprint.route("/<int:team_id>", methods=["DELETE"])
def delete_team_api(team_id):
    delete_team(team_id)
    return {"message": "you have successfully deleted user"}, 204
