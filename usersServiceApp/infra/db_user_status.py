from sqlalchemy import desc
from usersServiceApp.infra import create_in_db
from usersServiceApp.model import user_status


def create_user_status(id_user, my_user_status):
    my_user_status = my_user_status.lower()
    _user_status = user_status(id_user=id_user, user_status=my_user_status)
    create_in_db(_user_status)
    user_status_created = user_status.query.filter_by(
        id_user=_user_status.id_user).order_by(desc(user_status.date_created)).first()
    return user_status_created


def get_user_last_status(id_user):
    return user_status.query.filter_by(id_user=id_user).order_by(desc(user_status.date_created)).first().user_status
