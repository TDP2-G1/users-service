from flask import request, jsonify
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.admin_logic import validate_admin_credentials, validate_and_create_admin
from usersServiceApp.errors.usersException import usersException

bp_admin = Blueprint('admin', __name__, url_prefix='/admin/')


@bp_admin.route("", methods=['POST'])
@swag_from(methods=['POST'])
def register_new_admin_api():
    """
    Register admin
    The form has to be complete.
    ---
    tags:
      - admin
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - email
              - first_name
              - last_name
              - password
            properties:
              email:
                type: string
                description: Unique email representing the admin
              first_name:
                type: string
                description: first_name
              last_name:
                type: string
                description: Password
              password:
                type: string
                description: Password
    responses:
      200:
        description: A successful admin login
        schema:
          properties:
              token:
                type: string
                description: Token
    """
    try:
        post_data = request.get_json()
        token = validate_and_create_admin(post_data['email'], post_data['password'], post_data['first_name'],
                                          post_data['last_name'])
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'token': token}), 200


@bp_admin.route("/login", methods=['POST'])
@swag_from(methods=['POST'])
def login_admin_api():
    """
    Login admin
    The form has to be complete.
    ---
    tags:
      - admin
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - email
              - password
            properties:
              email:
                type: string
                description: Unique email representing the admin
              password:
                type: string
                description: Password
    responses:
      200:
        description: A successful admin login
        schema:
          properties:
              token:
                type: string
                description: Token
    """
    try:
        post_data = request.get_json()
        token = validate_admin_credentials(post_data['email'], post_data['password'])
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'token': token}), 200
