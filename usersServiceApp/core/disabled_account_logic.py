from usersServiceApp.core.register_logic import validate_user_id_exists, get_user_pictures
from usersServiceApp.infra.db_disabled_account import create_disabled_account, get_user_last_status


def validate_and_create_disabled_account(post_data):
    validate_user_id_exists(post_data['id_user'])
    return create_disabled_account(post_data)


def is_disabled(id_user):
    _disabled_account = get_user_last_status(id_user)
    if (_disabled_account is not None) and (_disabled_account.is_disabled is True):
        return True
    return False
