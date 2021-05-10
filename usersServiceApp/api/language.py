from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.register_logic import validate_and_create_language
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

from usersServiceApp.infra.db_language import get_all_languages

bp_language = Blueprint('language', __name__, url_prefix='/language/')


@bp_language.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_language():
    """
    Register a new language
    The form has to be complete.
    ---
    tags:
      - language
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - language_description
            properties:
              language_description:
                type: string
                description: description of the new language.
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              language_description:
                type: string
                description:  description of the new language.
              id:
                type: integer
                description: Unique identifier of the created language
    """
    try:
        post_data = request.get_json()
        language_created = validate_and_create_language(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'id': language_created.id_language, "language_description": language_created.language_description}), 200


@bp_language.route("/", methods=['GET'])
@swag_from(methods=['GET'])
def all_languages():
    """
    Get all languages
    ---
    tags:
      - language
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: false
    responses:
      200:
        description: A list of languages created
    """
    languages = get_all_languages()
    list_languages = []
    for language in languages:
        lang = {
            'id_language': language.id_language,
            "language_description": language.language_description
        }
        list_languages.append(lang)
    return jsonify(list_languages), 200
