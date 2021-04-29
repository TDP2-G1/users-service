from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.register_logic import validate_and_create_level
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_level = Blueprint('level', __name__, url_prefix='/level/')


@bp_level.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_level():
    """
    Register a new level
    The form has to be complete.
    ---
    tags:
      - level
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - level_description
            properties:
              level_description:
                type: string
                description: description of the new level.
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              level_description:
                type: string
                description:  description of the new level.
              id:
                type: integer
                description: Unique identifier of the created level
    """
    try:
        post_data = request.get_json()
        level_created = validate_and_create_level(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'id': level_created.id_level, "level_description": level_created.level_description}), 200
