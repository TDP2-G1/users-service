from usersServiceApp.core.register_logic import validate_user_id_exists
from usersServiceApp.errors.reportError import existentReportTypeError
from usersServiceApp.infra.db_reports import create_report, create_report_type, get_report_type_by_description


def validate_and_create_report_type(post_data):
    if get_report_type_by_description(post_data['report_type_description']) is None:
        return create_report_type(post_data)
    else:
        raise existentReportTypeError


# def validate_and_create_report(post_data):
#     validate_user_id_exists(post_data['id_user_1'])
#     validate_user_id_exists(post_data['id_user_2'])
#     create_report(post_data['id_user_2'], post_data['id_user_1'])
# 
# 
# def get_reports(id_user_followed):
#     reports = get_reports_by_id(id_user_followed)
#     _reports = []
#     for report in reports:
#         _user_following = report.id_user_following
#         _reports.append(_user_following)
#     return _reports
