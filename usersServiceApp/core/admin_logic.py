import hashlib
import time

from usersServiceApp.errors.adminError import loginAdminError, registrationAdminError
from usersServiceApp.infra.db_admin import create_admin, get_password_by_admin_email


def validate_and_create_admin(email, password, first_name, last_name):
    if email == '' or password == '' or first_name == '' or last_name == '':
        raise registrationAdminError
    encoded_password = hashlib.md5(password.encode()).hexdigest()
    create_admin(email, encoded_password, first_name, last_name)
    return generate_token(email)


def validate_admin_credentials(email, password):
    if email == '' or password == '':
        raise loginAdminError
    encoded_password = hashlib.md5(password.encode()).hexdigest()
    database_password = get_password_by_admin_email(email)
    if encoded_password != database_password:
        raise loginAdminError
    return generate_token(email)


def generate_token(email):
    ts = time.time()
    return hashlib.md5((email + str(ts)).encode()).hexdigest()
