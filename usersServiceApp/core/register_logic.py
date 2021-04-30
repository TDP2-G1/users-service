import datetime
from usersServiceApp.errors.genreError import existentGenreError, notExistentGenreError
from usersServiceApp.errors.languageError import existentLanguageError, notExistentLanguageError
from usersServiceApp.errors.levelError import existentLevelError, notExistentLevelError
from usersServiceApp.errors.usersError import AgeUnder16Error
from usersServiceApp.infra.db_genre import create_genre, get_genre_by_description, get_genre_by_id
from usersServiceApp.infra.db_language import get_language_by_description, create_language, get_language_by_id, \
    add_spoken_language_native, add_spoken_language_practice, get_spoken_languages
from usersServiceApp.infra.db_level import get_level_by_description, create_level, get_level_by_id
from usersServiceApp.infra.db_profile_picture import add_profile_picture, get_profile_pictures
from usersServiceApp.infra.db_user import create_user


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
    validate_birthdate(post_data)


def register_user(post_data):
    validate_user_fields(post_data)
    _user = create_user(post_data)
    add_languages(_user.id_user, post_data)
    _spoken_languages = get_languages(_user.id_user)
    add_profile_picture(_user.id_user, post_data['profile_picture'])
    _profile_pictures = get_profile_pictures(_user.id_user)
    return _user, _spoken_languages, _profile_pictures


def add_languages(id_user, post_data):
    if post_data['practice_language']:
        add_spoken_language_practice(id_user=id_user, id_language=post_data['practice_language'],
                                     id_level=post_data['actual_level'])
    if post_data['native_language']:
        add_spoken_language_native(id_user=id_user, id_language=post_data['native_language'])


def get_languages(id_user):
    return get_spoken_languages(id_user)


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


def validate_birthdate(post_data):
    d = datetime.datetime.strptime(post_data['birth_date'], "%d/%m/%Y")
    if calculate_age(d) < 16:
        raise AgeUnder16Error


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
