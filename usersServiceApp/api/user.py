from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.register_logic import validate_user_fields
from usersServiceApp.errors.usersException import usersException
from usersServiceApp.infra.db_user import create_user
from flask import jsonify

bp_user = Blueprint('user', __name__, url_prefix='/user/')


@bp_user.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def register_new_user_api():
    """
    Register a new user
    The form has to be complete.
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - first_name
              - last_name
              - birth_date
              - email
              - genre
              - profile_picture
              - native_language
              - practice_language
              - actual_level
              - topics_descriptions
            properties:
              first_name:
                type: string
                description: First name of the new user.
              last_name:
                type: string
                description: Last name of the new user.
              birth_date:
                type: string
                description: Birthday.
              email:
                type: string
                description: Unique email representing the new user - BookBnb, Admin
              genre:
                type: integer
                description: id of the genre (genre table)
              profile_picture:
                type: string
                description: Url of the profile picture on firebase
              native_language:
                type: integer
                description: id of the native language (language table)
              practice_language:
                type: integer
                description: id of the practice language (language table)
              actual_level:
                type: integer
                description: id of the actual level (level table)
              topics_descriptions:
                type: string
                description: Max 140 chars of topics
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              email:
                type: string
                description: Unique email of the created user
              id:
                type: integer
                description: Unique identifier of the created user
    """
    try:
        post_data = request.get_json()
        validate_user_fields(post_data)
        create_user(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'Status': "OK"}), 200
