from usersServiceApp.core.register_logic import validate_user_id_exists
from usersServiceApp.infra.db_block import create_block, get_blocks_by_id, get_blocked_by_id


def validate_and_create_block(post_data):
    validate_user_id_exists(post_data['id_user_blocker'])
    validate_user_id_exists(post_data['id_user_blocked'])
    create_block(post_data['id_user_blocker'], post_data['id_user_blocked'])


def get_blocks(id_user):
    blocks = get_blocks_by_id(id_user)
    blocked_by = get_blocked_by_id(id_user)
    _blocked = []
    _blocked_by = []
    for block in blocks:
        _user_ = block.id_user_blocker
        _blocked.append(_user_)
    for block in blocked_by:
        _user_ = block.id_user_blocked
        _blocked_by.append(_user_)
    return _blocked, _blocked_by, list(set(_blocked + _blocked_by))
