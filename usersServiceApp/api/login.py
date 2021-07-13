from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.login_logic import validate_and_log, get_logs_formated
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_login = Blueprint('login', __name__, url_prefix='/login/')


@bp_login.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_login():
    """
    Register a new login
    The form has to be complete.
    ---
    tags:
      - login
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - id_user
            properties:
              id_user:
                type: integer
                description: id_user
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              id:
                type: integer
                description: Unique identifier of the created login
    """
    try:
        post_data = request.get_json()
        validate_and_log(post_data['id_user'])
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'Status': 'logged'}), 200


@bp_login.route("/dataset", methods=['GET'])
@swag_from(methods=['GET'])
def get_user_if_registered():
    """
    Get user if registered
    ---
    tags:
      - login
    responses:
      200:
        description: A single user info if registered
        schema:
          properties:
              id:
                type: integer
                description: Unique identifier of the created user
    """
    try:
        _logins = get_logs_formated()
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(_logins), 200
