from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.feedback_logic import validate_and_create_feedback, get_feedbacks_info
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_feedback = Blueprint('feedback', __name__, url_prefix='/feedback/')


@bp_feedback.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_feedback():
    """
    Register a new feedback
    The form has to be complete.
    ---
    tags:
      - feedback
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - id_user_receiver
              - id_user_giver
              - feedback_description
            properties:
              id_user_receiver:
                type: integer
                description: id_user_receiver
              id_user_giver:
                type: integer
                description: id_user_giver
              feedback_description:
                type: string
                description: description of the new feedback.
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              feedback_description:
                type: string
                description:  description of the new feedback.
              id:
                type: integer
                description: Unique identifier of the created feedback
    """
    try:
        post_data = request.get_json()
        feedback_created = validate_and_create_feedback(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'id': feedback_created.id_feedback, "feedback_description": feedback_created.feedback_description}), 200


@bp_feedback.route("/<int:user_id>", methods=['GET'])
@swag_from(methods=['GET'])
def get_user_if_registered(user_id):
    """
    Get user if registered
    ---
    tags:
      - feedback
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
              first_name:
                type: string
                description: first name of the created user
    """
    try:
        _feedbacks = get_feedbacks_info(user_id)
        print(_feedbacks)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(_feedbacks), 200
