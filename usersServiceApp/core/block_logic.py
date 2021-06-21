from usersServiceApp.core.register_logic import validate_user_id_exists
from usersServiceApp.infra.db_block import create_block, get_blocks_by_id, get_blocked_by_id


def validate_and_create_block(post_data):
    validate_user_id_exists(post_data['id_user_blocker'])
    validate_user_id_exists(post_data['id_user_blocked'])
    create_block(post_data['id_user_blocker'], post_data['id_user_blocked'])


def get_blocks(id_user):
    blocks = get_blocks_by_id(id_user)
    print(blocks)
    blocked_by = get_blocked_by_id(id_user)
    print(blocked_by)
    _blocks = []
    for block in blocks:
        _user_ = block.id_user_blocker
        _blocks.append(_user_)
    for block in blocked_by:
        _user_ = block.id_user_blocked
        _blocks.append(_user_)
    return list(set(_blocks))
