from usersServiceApp.infra import create_in_db
from usersServiceApp.model import admin


def create_admin(email, encoded_password, first_name, last_name):
    _admin = admin(email=email, password=encoded_password, first_name=first_name, last_name=last_name)
    return create_in_db(_admin)


def get_password_by_admin_email(email):
    return admin.query.filter_by(email=email).first().password


def get_admin_by_email(email):
    return admin.query.filter_by(email=email).first()

