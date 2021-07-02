from usersServiceApp import database
from usersServiceApp.infra import create_in_db
from usersServiceApp.model import block


def create_block(id_user_1, id_user_2):
    _block = block(id_user_blocker=id_user_1, id_user_blocked=id_user_2)
    return create_in_db(_block)


def delete_block(id_user_1, id_user_2):
    block.query.filter_by(id_user_blocker=id_user_1, id_user_blocked=id_user_2).delete()
    database.db.session.commit()


def block_exists(id_user_1, id_user_2):
    _block = block.query.filter_by(id_user_blocker=id_user_1, id_user_blocked=id_user_2).first()
    if _block is not None:
        return True
    return False

def get_blocks_by_id(id_user_blocked):
    return block.query.filter_by(id_user_blocked=id_user_blocked).all()


def get_blocked_by_id(id_user_blocker):
    return block.query.filter_by(id_user_blocker=id_user_blocker).all()
