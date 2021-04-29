from usersServiceApp.errors.genreError import existentGenreError
from usersServiceApp.errors.languageError import existentLanguageError
from usersServiceApp.errors.levelError import existentLevelError
from usersServiceApp.infra.db_genre import create_genre, get_genre_by_description
from usersServiceApp.infra.db_language import get_language_by_description, create_language
from usersServiceApp.infra.db_level import get_level_by_description, create_level


def validate_user_fields(post_data):
    return True


def validate_existent_genre(description):
    if get_genre_by_description(description) is not None:
        raise existentGenreError


def validate_and_create_genre(post_data):
    validate_existent_genre(post_data['genre_description'])
    return create_genre(post_data)


def validate_existent_language(description):
    if get_language_by_description(description) is not None:
        raise existentLanguageError


def validate_and_create_language(post_data):
    validate_existent_language(post_data['language_description'])
    return create_language(post_data)


def validate_existent_level(description):
    if get_level_by_description(description) is not None:
        raise existentLevelError


def validate_and_create_level(post_data):
    validate_existent_level(post_data['level_description'])
    return create_level(post_data)