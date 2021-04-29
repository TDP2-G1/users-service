from usersServiceApp.infra import create_in_db
from usersServiceApp.model import level


def create_level(post_data):
    _level = level(level_description=post_data['level_description'])
    create_in_db(_level)
    level_created = level.query.filter_by(level_description=_level.level_description).first()
    return level_created


def get_level_by_description(description):
    return level.query.filter(level.level_description.ilike(description)).first()


def get_level_by_id(id_level):
    return level.query.filter_by(id_level=id_level).first()