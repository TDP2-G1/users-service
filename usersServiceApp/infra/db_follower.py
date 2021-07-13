from usersServiceApp.infra import create_in_db
from usersServiceApp.model import follower


def create_follower(id_user_1, id_user_2):
    _follower = follower(id_user_followed=id_user_1, id_user_following=id_user_2)
    create_in_db(_follower)


def get_followers_by_id(id_user_followed):
    return follower.query.filter_by(id_user_followed=id_user_followed).all()


def get_followers_relation(id_user_1, id_user_2):
    return follower.query.filter_by(id_user_followed=id_user_1, id_user_following=id_user_2).first()
