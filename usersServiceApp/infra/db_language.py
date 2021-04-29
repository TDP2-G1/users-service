from usersServiceApp.infra import create_in_db
from usersServiceApp.model import language


def create_language(post_data):
    _language = language(language_description=post_data['language_description'])
    create_in_db(_language)
    language_created = language.query.filter_by(language_description=_language.language_description).first()
    return language_created


def get_language_by_description(description):
    return language.query.filter(language.language_description.ilike(description)).first()
