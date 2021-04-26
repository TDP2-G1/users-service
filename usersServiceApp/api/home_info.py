from usersServiceApp.Errors.usersException import usersException
from flask import Blueprint, current_app
from flask import jsonify, render_template
from flasgger.utils import swag_from


bp_homeinfo = Blueprint('status_info', __name__, url_prefix='/')


@bp_homeinfo.route("/", methods=['GET'])
@swag_from(methods=['GET'])
def home():
    return render_template("home.html")


@bp_homeinfo.route("/health", methods=['GET'])
@swag_from(methods=['GET'])
def health():
    """
    Health Check
    To Know if the APP is UP and running.
    ---
    tags:
      - health
    responses:
      200:
        description: Status
    """

    return jsonify({"status": "UP", "from": "usersServiceApp"}), 200
