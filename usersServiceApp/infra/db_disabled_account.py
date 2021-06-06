from sqlalchemy import desc, func, select
from sqlalchemy.orm import session

from usersServiceApp.infra import create_in_db
from usersServiceApp.model import disabled_account


def create_disabled_account(post_data):
    _disabled_account = disabled_account(id_user=post_data['id_user'], is_disabled=post_data['is_disabled'])
    create_in_db(_disabled_account)
    disabled_account_created = disabled_account.query.filter_by(id_user=_disabled_account.id_user).order_by(desc(disabled_account.date_created)).first()
    return disabled_account_created


def get_user_last_status(id_user):
    return disabled_account.query.filter_by(id_user=id_user).order_by(desc(disabled_account.date_created)).first()
