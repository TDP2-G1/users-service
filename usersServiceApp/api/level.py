from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.register_logic import validate_and_create_level
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

from usersServiceApp.infra.db_level import get_all_levels

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


@bp_level.route("/", methods=['GET'])
@swag_from(methods=['GET'])
def all_levels():
    """
    Get all levels
    ---
    tags:
      - level
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: false
    responses:
      200:
        description: A list of levels created
    """
    levels = get_all_levels()
    list_levels = []
    for level in levels:
        lang = {
            'id_level': level.id_level,
            "level_description": level.level_description
        }
        list_levels.append(lang)
    return jsonify(list_levels), 200
