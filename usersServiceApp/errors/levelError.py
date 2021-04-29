from flask import current_app
from usersServiceApp.errors.usersException import usersException


class existentLevelError(usersException):
    def __init__(self, message="level already exists in database."):
        current_app.logger.error("level already exists in database.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class notExistentLevelError(usersException):
    def __init__(self, message="Level doesn't exists."):
        current_app.logger.error("Level doesn't exists.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)
