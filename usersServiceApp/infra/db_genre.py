from usersServiceApp.infra import create_in_db
from usersServiceApp.model import genre


def create_genre(post_data):
    _genre = genre(genre_description=post_data['genre_description'])
    create_in_db(_genre)
    genre_created = genre.query.filter_by(genre_description=_genre.genre_description).first()
    return genre_created


def get_genre_by_description(description):
    return genre.query.filter(genre.genre_description.ilike(description)).first()


def get_genre_by_id(id_genre):
    return genre.query.filter_by(id_genre=id_genre).first()