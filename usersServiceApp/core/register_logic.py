from usersServiceApp.errors.genreError import existentGenreError
from usersServiceApp.infra.db_genre import create_genre, get_genre_by_description


def validate_user_fields(post_data):
    return True


def validate_existent_genre(description):
    if get_genre_by_description(description) is not None:
        raise existentGenreError


def validate_and_create_genre(post_data):
    validate_existent_genre(post_data['genre_description'])
    return create_genre(post_data)
