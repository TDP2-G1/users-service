from flask import request
from flasgger.utils import swag_from
from flask import Blueprint

from usersServiceApp.core.report_logic import validate_and_create_report_type
from usersServiceApp.errors.usersException import usersException
from flask import jsonify

from usersServiceApp.infra.db_reports import get_all_report_types

bp_report_type = Blueprint('report_type', __name__, url_prefix='/report_type/')


@bp_report_type.route("/", methods=['POST'])
@swag_from(methods=['POST'])
def new_report_type():
    """
    Register a new report_type
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
              - report_type_description
            properties:
              report_type_description:
                type: string
                description: description of the new report_type.
    responses:
      200:
        description: A successful profile creation
        schema:
          properties:
              report_type_description:
                type: string
                description:  description of the new report_type.
              id:
                type: integer
                description: Unique identifier of the created report_type
    """
    try:
        post_data = request.get_json()
        report_type_created = validate_and_create_report_type(post_data)
    except usersException as e:
        return jsonify({'Error': e.message}), e.error_code
    return jsonify({'id': report_type_created.id_report_type,
                    "report_type_description": report_type_created.report_type_description}), 200


@bp_report_type.route("/", methods=['GET'])
@swag_from(methods=['GET'])
def all_report_types():
    """
    Get all report_types
    ---
    tags:
      - report
    consumes:
      - application/json
    parameters:
      - name: body
        in: body
        required: false
    responses:
      200:
        description: A list of report_types created
    """
    report_types = get_all_report_types()
    print(report_types)
    list_report_types = []
    for report_type in report_types:
        lang = {
            'id_report_type': report_type.id_report_type,
            "report_type_description": report_type.report_type_description
        }
        print(lang)
        list_report_types.append(lang)
    return jsonify(list_report_types), 200
