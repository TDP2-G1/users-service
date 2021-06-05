from usersServiceApp.core.register_logic import validate_user_id_exists, get_user_pictures
from usersServiceApp.errors.reportError import existentReportTypeError
from usersServiceApp.infra.db_reports import create_report, create_report_type, get_report_type_by_description, \
    get_report_by_user_reported, get_report_type_by_id
from usersServiceApp.infra.db_user import get_user_by_id


def validate_and_create_report_type(post_data):
    if get_report_type_by_description(post_data['report_type_description']) is None:
        return create_report_type(post_data)
    else:
        raise existentReportTypeError


def validate_and_create_report(post_data):
    validate_user_id_exists(post_data['id_user_reported'])
    validate_user_id_exists(post_data['id_user_reported_by'])
    return create_report(post_data['id_report_type'], post_data['id_user_reported']
                         , post_data['id_user_reported_by'])


def get_reports_info(id_user_reported):
    reports = get_report_by_user_reported(id_user_reported)
    _reports = []
    for report in reports:
        _user_reported_by = get_user_by_id(report.id_user_reported_by)
        _reports.append(format_report(report, _user_reported_by))
    return _reports


def format_report(report, _user_reported_by):
    pictures = get_user_pictures(_user_reported_by.id_user)
    _report = {
        "id_report": report.id_report,
        "id_user_reported_by": _user_reported_by.id_user,
        "first_name": _user_reported_by.first_name,
        "profile_picture": pictures[0].url_picture,
        "report_description": (get_report_type_by_id(report.id_report_type)).report_type_description,
        "date": report.date_created.strftime("%d/%m/%Y")
    }
    return _report


def get_reports(id_user_reported):
    reports = get_report_by_user_reported(id_user_reported)
    _reports = []
    for report in reports:
        _user_reported_by = report.id_user_reported_by
        _reports.append(_user_reported_by)
    return list(set(_reports))
