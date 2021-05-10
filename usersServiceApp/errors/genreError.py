from flask import current_app
from usersServiceApp.errors.usersException import usersException


class existentGenreError(usersException):
    def __init__(self, message="Genre already exists in database."):
        current_app.logger.error("Genre already exists in database.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class notExistentGenreError(usersException):
    def __init__(self, message="Genre doesn't exists."):
        current_app.logger.error("Genre doesn't exists.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)