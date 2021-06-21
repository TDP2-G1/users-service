from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.block_logic import validate_and_create_block, get_blocks
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_block = Blueprint('block', __name__, url_prefix='/block/')


@bp_block.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_block():
    """
    Register a new block
    The form has to be complete.
    ---
    tags:
      - block
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - id_user_blocker
              - id_user_blocked
            properties:
              id_user_blocker:
                type: integer
                description: id_user_blocker
              id_user_blocked:
                type: integer
                description: id_user_blocked
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              id:
                type: integer
                description: Unique identifier of the created block
    """
    try:
        post_data = request.get_json()
        validate_and_create_block(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'id_1': post_data['id_user_blocker'], 'id_2': post_data['id_user_blocked']}), 200


@bp_block.route("/<int:user_id>", methods=['GET'])
@swag_from(methods=['GET'])
def get_user_if_registered(user_id):
    """
    Get users blocks
    ---
    tags:
      - block
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
        _blocks = get_blocks(user_id)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(_blocks), 200
