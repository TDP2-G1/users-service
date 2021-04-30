from usersServiceApp.infra import create_in_db
from usersServiceApp.model import language, spoken_language


def create_language(post_data):
    _language = language(language_description=post_data['language_description'])
    create_in_db(_language)
    language_created = language.query.filter_by(language_description=_language.language_description).first()
    return language_created


def get_language_by_description(description):
    return language.query.filter(language.language_description.ilike(description)).first()


def get_language_by_id(id_language):
    return language.query.filter_by(id_language=id_language).first()


def add_spoken_language_native(id_user, id_language, id_level=None):
    _spoken_language = spoken_language(id_user=id_user, id_language=id_language, id_level=id_level, is_native=True)
    create_in_db(_spoken_language)


def add_spoken_language_practice(id_user, id_language, id_level):
    _spoken_language = spoken_language(id_user=id_user, id_language=id_language, id_level=id_level, is_native=False)
    create_in_db(_spoken_language)


def get_spoken_languages(id_user):
    return spoken_language.query.filter_by(id_user=id_user).all()