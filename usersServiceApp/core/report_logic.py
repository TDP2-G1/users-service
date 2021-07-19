import datetime

from usersServiceApp.core.register_logic import validate_user_id_exists, get_user_pictures
from usersServiceApp.errors.reportError import existentReportTypeError, notExistentIdReportError
from usersServiceApp.infra.db_reports import create_report, create_report_type, get_report_type_by_description, \
    get_report_by_user_reported, get_report_type_by_id, create_report_text, get_text_report_by_id, \
    get_status_report_by_id, get_report_by_id, create_report_status, delete_report_status, get_all_reports
from usersServiceApp.infra.db_user import get_user_by_id


def validate_and_create_report_type(post_data):
    if get_report_type_by_description(post_data['report_type_description']) is None:
        return create_report_type(post_data)
    else:
        raise existentReportTypeError


def validate_and_create_report(post_data):
    validate_user_id_exists(post_data['id_user_reported'])
    validate_user_id_exists(post_data['id_user_reported_by'])
    _report_created = create_report(post_data['id_report_type'], post_data['id_user_reported']
                                    , post_data['id_user_reported_by'])
    if 'other_text' in post_data and post_data['other_text']:
        create_report_text(_report_created.id_report, post_data['other_text'])
    validate_and_update_report_status(_report_created.id_report, True)


def get_reports_info(id_user_reported):
    reports = get_report_by_user_reported(id_user_reported)
    _reports = []
    for report in reports:
        _user_reported_by = get_user_by_id(report.id_user_reported_by)
        _reports.append(format_report(report, _user_reported_by))
    get_report_status_dataset()
    return _reports


def format_report(report, _user_reported_by):
    pictures = get_user_pictures(_user_reported_by.id_user)
    _text = ""
    if get_text_report_by_id(report.id_report) is not None:
        _text = get_text_report_by_id(report.id_report).report_text

    _status = True
    if get_status_report_by_id(report.id_report) is not None:
        _status = get_status_report_by_id(report.id_report).is_pending

    _report = {
        "id_report": report.id_report,
        "id_user_reported_by": _user_reported_by.id_user,
        "first_name": _user_reported_by.first_name,
        "profile_picture": pictures[0].url_picture,
        "report_description": (get_report_type_by_id(report.id_report_type)).report_type_description,
        "text": _text,
        "date": report.date_created.strftime("%d/%m/%Y"),
        "is_pending": _status
    }
    return _report


def get_reports(id_user_reported):
    reports = get_report_by_user_reported(id_user_reported)
    _reports = []
    for report in reports:
        _user_reported_by = report.id_user_reported_by
        _reports.append(_user_reported_by)
    return list(set(_reports))


def get_reports_with_status(id_user_reported):
    reports = get_report_by_user_reported(id_user_reported)
    _reports = []
    for report in reports:
        pending = True
        if get_status_report_by_id(report.id_report) is not None:
            pending = get_status_report_by_id(report.id_report).is_pending
        _data = {
            'user_reported_by': report.id_user_reported_by,
            'is_pending': pending
        }
        _reports.append(_data)
    return _reports


def validate_and_update_report_status(id_report, is_pending):
    if get_report_by_id(id_report) is None:
        raise notExistentIdReportError
    if get_status_report_by_id(id_report) is not None:
        delete_report_status(id_report)
    create_report_status(id_report, is_pending)


def get_report_status_dataset():
    _reports = get_all_reports()
    _dataset = {}
    for report in _reports:
        pending = True
        if get_status_report_by_id(report.id_report) is not None:
            pending = get_status_report_by_id(report.id_report).is_pending
        month_year = str(report.date_created.month) + "/" + str(report.date_created.year)
        if month_year in _dataset:
            _dataset[month_year]['abiertas'] = _dataset[month_year]['abiertas'] + 1
            if pending and 'pendientes' in _dataset[month_year]:
                _dataset[month_year]['pendientes'] = _dataset[month_year]['pendientes'] + 1
            else:
                _dataset[month_year]['pendientes'] = 1
        else:
            _dataset[month_year] = {"abiertas": 1}
            if pending: _dataset[month_year]['pendientes'] = 1
    nuevo = []
    for month_year in _dataset:
        nuevo.append(format_report_status(month_year, _dataset[month_year]))
    return nuevo


def format_report_status(month_year, log):
    month = month_year.split("/")[0]
    year = month_year.split("/")[1]
    abiertas = log['abiertas']
    pendientes = 0
    if "pendientes" in log:
        pendientes = log["pendientes"]
    _data = {
        "month": int(month),
        "year": int(year),
        "abiertas": abiertas,
        "pendientes": pendientes
    }
    return _data
