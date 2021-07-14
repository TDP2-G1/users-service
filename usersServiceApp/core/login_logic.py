import time

from usersServiceApp.core.register_logic import validate_user_id_exists
from usersServiceApp.infra.db_log import create_log_login_user, get_logs


def validate_and_log(id_user):
    validate_user_id_exists(id_user)
    create_log_login_user(id_user)


def get_logs_formated():
    _logs = get_logs()
    _my_logs = {}
    for log in _logs:
        fl = format_log(log)
        if fl['date'] in _my_logs:
            if not fl['id_user'] in _my_logs[fl['date']]['users']:
                _my_logs[fl['date']]['users'].append(fl['id_user'])
        else:
            _my_logs[fl['date']] = {'users': [fl['id_user']]}
    nuevo = []
    for date in _my_logs:
        nuevo.append(format_dataset(date, _my_logs[date]))
    return nuevo


def format_log(log):
    _log = {
        "id_user": log.id_user,
        "date": log.date_created.strftime("%d/%m/%Y")
    }
    return _log


def format_dataset(date, log):
    _data = {
        "day": int(date[:2]),
        "month": int(date[3:5]),
        "year": int(date[6:10]),
        "active_users": len(log['users'])
    }
    return _data
