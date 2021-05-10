from usersServiceApp.infra import create_in_db
from usersServiceApp.model import profile_picture


def add_profile_picture(id_user, url):
    _profile_picture = profile_picture(id_user=id_user, url_picture=url)
    create_in_db(_profile_picture)


def get_profile_pictures(id_user):
    return profile_picture.query.filter_by(id_user=id_user).all()
