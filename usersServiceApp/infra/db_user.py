from usersServiceApp.infra import create_in_db
from usersServiceApp.model import user


def create_user(post_data):
    _user = user(first_name=post_data['first_name'], last_name=post_data['last_name'],
                 email=post_data['email'], genre=post_data['genre'],
                 native_language=post_data['native_language'], practice_language=post_data['practice_language'],
                 actual_level=post_data['actual_level'], topics_descriptions=post_data['topics_descriptions'])
    create_in_db(_user)
    user_created = user.query.filter_by(email=_user.email).first()
    return user_created
