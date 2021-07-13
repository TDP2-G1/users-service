from usersServiceApp.infra import create_in_db
from usersServiceApp.model import log_login_user


def create_log_login_user(id_user):
    _log_login_user = log_login_user(id_user=id_user)
    return create_in_db(_log_login_user)


def get_logs():
    return log_login_user.query.all()
