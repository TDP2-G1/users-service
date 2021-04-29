from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.register_logic import validate_and_create_genre
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_genre = Blueprint('genre', __name__, url_prefix='/genre/')


@bp_genre.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_genre():
    """
    Register a new genre
    The form has to be complete.
    ---
    tags:
      - genre
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - genre_description
            properties:
              genre_description:
                type: string
                description: description of the new genre.
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              genre_description:
                type: string
                description:  description of the new genre.
              id:
                type: integer
                description: Unique identifier of the created genre
    """
    try:
        post_data = request.get_json()
        genre_created = validate_and_create_genre(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'id': genre_created.id_genre, "genre_description": genre_created.genre_description}), 200
