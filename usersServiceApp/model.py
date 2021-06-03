from usersServiceApp.database import db


class user(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.DateTime)
    email = db.Column(db.String(255), unique=True, nullable=False)
    genre = db.Column(db.Integer, db.ForeignKey('genre.id_genre'), nullable=False)
    topics_descriptions = db.Column(db.String(140), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"user: {self.id_user}"


class fb_user(db.Model):
    fb_user_id = db.Column(db.String(250), primary_key=True, unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))

    def __repr__(self):
        return f"user: {self.id_user}"


class profile_picture(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, nullable=False)
    id_picture = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_picture = db.Column(db.String(200), nullable=False)

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


class spoken_language(db.Model):
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    id_language = db.Column(db.Integer, db.ForeignKey('language.id_language'), primary_key=True, nullable=False)
    is_native = db.Column(db.BOOLEAN, default=False, primary_key=True)
    id_level = db.Column(db.Integer, db.ForeignKey('level.id_level'), nullable=True)

    def __repr__(self):
        return f"spoken_language: {self.id_language}"


class level(db.Model):
    id_level = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    level_description = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"level: {self.id_level}"


class feedback(db.Model):
    id_feedback = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    id_user_receiver = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    id_user_giver = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    feedback_description = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return f"feedback: {self.id_feedback}"


class follower(db.Model):
    id_user_followed = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    id_user_following = db.Column(db.Integer, db.ForeignKey('user.id_user'), primary_key=True, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"follower: {self.id_user_following}"
