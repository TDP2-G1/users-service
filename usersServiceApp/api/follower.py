from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.follower_logic import validate_and_create_follower, get_followers
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_follower = Blueprint('follower', __name__, url_prefix='/follower/')


@bp_follower.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_follower():
    """
    Register a new follower
    The form has to be complete.
    ---
    tags:
      - follower
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - id_user_1
              - id_user_2
            properties:
              id_user_1:
                type: integer
                description: id_user_1
              id_user_2:
                type: integer
                description: id_user_2
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              id:
                type: integer
                description: Unique identifier of the created follower
    """
    try:
        post_data = request.get_json()
        validate_and_create_follower(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'id_1': post_data['id_user_1'], 'id_2': post_data['id_user_2']}), 200


@bp_follower.route("/<int:user_id>", methods=['GET'])
@swag_from(methods=['GET'])
def get_user_if_registered(user_id):
    """
    Get users followers
    ---
    tags:
      - follower
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
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
        _followers = get_followers(user_id)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(_followers), 200
