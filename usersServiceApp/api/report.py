from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.report_logic import validate_and_create_report, get_reports_info, \
    validate_and_update_report_status, get_report_status_dataset
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

bp_report = Blueprint('report', __name__, url_prefix='/report/')


@bp_report.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_report():
    """
    Register a new report
    The form has to be complete.
    ---
    tags:
      - report
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: true
        schema:
            required:
              - id_report_type
              - id_user_reported
              - id_user_reported_by
            properties:
              id_report_type:
                type: integer
                description: id_report_type
              id_user_reported:
                type: integer
                description: id_user_reported
              id_user_reported_by:
                type: integer
                description: id_user_reported_by
              other_text:
                type: String
                description: text for other report
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              id:
                type: integer
                description: Unique identifier of the created report
    """
    try:
        post_data = request.get_json()
        validate_and_create_report(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'Status': "Report Created"}), 200


@bp_report.route("/<int:user_id>", methods=['GET'])
@swag_from(methods=['GET'])
def get_user_if_registered(user_id):
    """
    Get user if registered
    ---
    tags:
      - report
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
        _reports = get_reports_info(user_id)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(_reports), 200


@bp_report.route("/<int:report_id>", methods=['PUT'])
@swag_from(methods=['PUT'])
def update_report(report_id):
    """
    update status report
    The form has to be complete.
    ---
    tags:
      - report
    consumes:
      - application/json
    parameters:
      - in: path
        name: report_id
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
            required:
              - is_pending
            properties:
              is_pending:
                type: boolean
                description: is_pending
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              id:
                type: integer
                description: Unique identifier of the updated report
    """
    try:
        post_data = request.get_json()
        validate_and_update_report_status(report_id, post_data['is_pending'])
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(
        {'Status': "Report Updated"}), 200


@bp_report.route("/dataset", methods=['GET'])
@swag_from(methods=['GET'])
def get_report_dataset():
    """
    Get dataset
    ---
    tags:
      - report
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
        _reports = get_report_status_dataset()
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify(_reports), 200
