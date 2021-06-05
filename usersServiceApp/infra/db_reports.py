from usersServiceApp.infra import create_in_db
from usersServiceApp.model import report, report_type


def create_report_type(post_data):
    _report_type = report_type(report_type_description=post_data['report_type_description'])
    create_in_db(_report_type)
    return report_type.query.filter_by(report_type_description=_report_type.report_type_description).first()


def get_report_type_by_description(description):
    return report_type.query.filter(report_type.report_type_description.ilike(description)).first()


def get_report_type_by_id(id_report_type):
    return report_type.query.filter_by(id_report_type=id_report_type).first()


def get_all_report_types():
    return report_type.query.all()


def create_report(id_report_type, id_user_reported, id_user_reported_by):
    _report = report(id_report_type=id_report_type, id_user_reported=id_user_reported,
                     id_user_reported_by=id_user_reported_by)
    create_in_db(_report)
    return True


def get_report_by_user_reported(id_user_reported):
    return report.query.filter_by(id_user_reported=id_user_reported).all()


def get_report_by_id(id_report):
    return report.query.filter_by(id_report=id_report).first()


def get_all_reports():
    return report.query.all()
