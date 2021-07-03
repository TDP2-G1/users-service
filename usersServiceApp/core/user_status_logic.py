from usersServiceApp.core.register_logic import validate_user_id_exists
from usersServiceApp.errors.usersError import EmptyUserStatusError
from usersServiceApp.infra.db_user_status import create_user_status, get_user_last_status


def validate_and_create_user_status(id_user, post_data):
    if 'user_status' not in post_data or post_data['user_status'] == '':
        raise EmptyUserStatusError
    else:
        user_status = post_data['user_status']
    validate_user_id_exists(id_user)
    return create_user_status(id_user, user_status)


def get_user_last_status_logic(id_user):
    _status = get_user_last_status(id_user)
    if _status is None:
        _status = 'online'
    return _status
