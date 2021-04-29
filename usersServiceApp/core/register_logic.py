from usersServiceApp.errors.genreError import existentGenreError, notExistentGenreError
from usersServiceApp.errors.languageError import existentLanguageError, notExistentLanguageError
from usersServiceApp.errors.levelError import existentLevelError, notExistentLevelError
from usersServiceApp.infra.db_genre import create_genre, get_genre_by_description, get_genre_by_id
from usersServiceApp.infra.db_language import get_language_by_description, create_language, get_language_by_id
from usersServiceApp.infra.db_level import get_level_by_description, create_level, get_level_by_id


def validate_genre_by_id(id_genre):
    if get_genre_by_id(id_genre) is None:
        raise notExistentGenreError


def validate_language_by_id(id_language):
    if get_language_by_id(id_language) is None:
        raise notExistentLanguageError


def validate_level_by_id(id_level):
    if get_level_by_id(id_level) is None:
        raise notExistentLevelError


def validate_user_fields(post_data):
    validate_genre_by_id(post_data['genre'])
    validate_language_by_id(post_data['native_language'])
    validate_language_by_id(post_data['practice_language'])
    validate_level_by_id(post_data['actual_level'])


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