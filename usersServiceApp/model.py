from usersServiceApp.database import db


class user(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    email = db.Column(db.String(255), unique=True, nullable=False)
    genre = db.Column(db.Integer, db.ForeignKey('genre.id_genre'), nullable=False)
    native_language = db.Column(db.Integer, db.ForeignKey('language.id_language'), nullable=False)
    practice_language = db.Column(db.Integer, db.ForeignKey('language.id_language'), nullable=False)
    actual_level = db.Column(db.Integer, db.ForeignKey('level.id_level'), nullable=False)
    topics_descriptions = db.Column(db.String(140), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"user: {self.id_user}"


class profile_picture(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    id_picture = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_picture = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"profile_picture: {self.id_user, self.id_picture}"


class genre(db.Model):
    id_genre = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    genre_description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"genre: {self.id_genre}"


class language(db.Model):
    id_language = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    language_description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"language: {self.id_language}"


class level(db.Model):
    id_level = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    level_description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"level: {self.id_level}"


def insert_initial_values():
    #db.session.add(genre(genre_description='default'))
    #db.session.add(language(language_description='default'))
    #db.session.add(level(level_description='default'))
    #db.session.commit()
    return True




