from flask import current_app
from usersServiceApp.errors.usersException import usersException


class existentGenreError(usersException):
    def __init__(self, message="Genre already exists in database."):
        current_app.logger.error("Genre already exists in database.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)

