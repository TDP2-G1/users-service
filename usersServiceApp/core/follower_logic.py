from usersServiceApp.core.register_logic import validate_user_id_exists
from usersServiceApp.infra.db_follower import create_follower, get_followers_by_id, get_followers_relation


def validate_and_create_follower(post_data):
    validate_user_id_exists(post_data['id_user_1'])
    validate_user_id_exists(post_data['id_user_2'])
    if not exists_relation(post_data['id_user_1'], post_data['id_user_2']):
        create_follower(post_data['id_user_1'], post_data['id_user_2'])
    if not exists_relation(post_data['id_user_2'], post_data['id_user_1']):
        create_follower(post_data['id_user_2'], post_data['id_user_1'])


def exists_relation(id_user_1, id_user_2):
    return get_followers_relation(id_user_1, id_user_2) is not None


def get_followers(id_user_followed):
    followers = get_followers_by_id(id_user_followed)
    _followers = []
    for follower in followers:
        _user_following = follower.id_user_following
        _followers.append(_user_following)
    return _followers
