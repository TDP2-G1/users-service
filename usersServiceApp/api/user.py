from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.block_logic import get_blocks
from usersServiceApp.core.disabled_account_logic import is_disabled, validate_and_create_disabled_account
from usersServiceApp.core.follower_logic import get_followers
from usersServiceApp.core.register_logic import register_user, \
    get_user_info_by_fb_user_id, get_languages, get_user_pictures
from usersServiceApp.core.report_logic import get_reports
from usersServiceApp.core.user_status_logic import get_user_last_status_logic, validate_and_create_user_status
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

from usersServiceApp.infra.db_block import get_blocked_by_id, get_blocks_by_id
from usersServiceApp.infra.db_disabled_account import create_disabled_account
from usersServiceApp.infra.db_feedback import get_user_amount_received_feedbacks
from usersServiceApp.infra.db_user import get_all_users, get_fb_user_by_user_id

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
              - fb_user_id
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
              fb_user_id:
                type: string
                description: Unique id for the user on FB.
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
        post_data['fb_user_id'] = str(post_data['fb_user_id'])
        _user, _spoken_languages, _profile_pictures = register_user(post_data)
        formated_languages = format_languages(_spoken_languages)
        formated_pictures = format_pictures(_profile_pictures)
        formated_user = format_user(_user, formated_languages, formated_pictures)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(formated_user), 200


def format_user(_user, languages=None, pictures=None):
    if languages is None:
        languages = format_languages(get_languages(_user.id_user))
    if pictures is None:
        pictures = format_pictures(get_user_pictures(_user.id_user))
    amount_feedbacks = get_user_amount_received_feedbacks(_user.id_user)
    my_fb_user_id = get_fb_user_by_user_id(_user.id_user).fb_user_id
    _followers = get_followers(_user.id_user)
    _reported_by = get_reports(_user.id_user)
    _is_disabled = is_disabled(_user.id_user)
    _blocked, _blocked_by, another = get_blocks(_user.id_user)
    _user_status = get_user_last_status_logic(_user.id_user)

    _user = {'id_user': _user.id_user,
             "birth_date": _user.birth_date.strftime("%d/%m/%Y"),
             "email": _user.email,
             "first_name": _user.first_name,
             "last_name": _user.last_name,
             "genre": _user.genre,
             "profile_picture": "string",
             "topics_descriptions": _user.topics_descriptions,
             "languages": languages,
             "pictures": pictures,
             "amount_feedbacks": amount_feedbacks,
             "fb_user_id": my_fb_user_id,
             "followers": _followers,
             "reported_by": _reported_by,
             "is_disabled": _is_disabled,
             "blocked_by": _blocked_by,
             "blocked": _blocked,
             "user_status": _user_status
             }
    return _user


def format_languages(_spoken_languages):
    languages = []
    for _language in _spoken_languages:
        _language = {
            'id_user': _language.id_user,
            'id_language': _language.id_language,
            'id_level': _language.id_level,
            'is_native': _language.is_native
        }
        languages.append(_language)
    return languages


def format_pictures(_profile_pictures):
    pictures = []
    for _picture in _profile_pictures:
        _picture = {
            'id_user': _picture.id_user,
            'id_picture': _picture.id_picture,
            'url': _picture.url_picture
        }
        pictures.append(_picture)
    return pictures


@bp_user.route("/", methods=['GET'])
@swag_from(methods=['GET'])
def all_users(user_id=None):
    """
    Get all users
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: int
        required: false
    responses:
      200:
        description: A list of users created
    """
    users = get_all_users()
    list_users = []
    for _user in users:
        if _user.id_user != user_id:
            _formated_user = format_user(_user)
            list_users.append(_formated_user)
    return jsonify(list_users), 200


@bp_user.route("/<string:fb_user_id>", methods=['GET'])
@swag_from(methods=['GET'])
def get_user_if_registered(fb_user_id):
    """
    Get user if registered
    ---
    tags:
      - user
    parameters:
      - in: path
        name: fb_user_id
        type: string
        required: true
    responses:
      200:
        description: A single user info if registered
        schema:
          properties:
              email:
                type: string
                description: Unique email of the created user
              id:
                type: integer
                description: Unique identifier of the created user
              first_name:
                type: string
                description: first name of the created user
              last_name:
                type: string
                description: last name of the created user
    """
    try:
        _user = get_user_info_by_fb_user_id(str(fb_user_id))
        formated_user = format_user(_user)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(formated_user), 200


@bp_user.route("/<int:user_id>/account_status", methods=['PUT'])
@swag_from(methods=['PUT'])
def new_status(user_id):
    """
    Change status for user's by id
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
            required:
              - is_disabled
            properties:
              is_disabled:
                type: boolean
                description: New disabled status.
    responses:
      200:
        description: A successful change of user blocked status.
        schema:
          properties:
              user_id:
                type: integer
                description: Unique identifier representing the user.
    """
    try:
        post_data = request.get_json()
        post_data['id_user'] = user_id
        _return = validate_and_create_disabled_account(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'Status': 'Updated'}), 200


@bp_user.route("/<int:user_id>/user_status", methods=['PUT'])
@swag_from(methods=['PUT'])
def new_user_status(user_id):
    """
    Change status for user's by id
    ---
    tags:
      - user
    consumes:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
            required:
              - user_status
            properties:
              user_status:
                type: string
                description: New user status.
    responses:
      200:
        description: A successful change of user status.
        schema:
          properties:
              user_id:
                type: integer
                description: Unique identifier representing the user.
    """
    try:
        post_data = request.get_json()
        post_data['id_user'] = user_id
        _return = validate_and_create_user_status(user_id, post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'Status': 'Updated'}), 200
