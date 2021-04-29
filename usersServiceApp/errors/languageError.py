from flask import current_app
from usersServiceApp.errors.usersException import usersException


class existentLanguageError(usersException):
    def __init__(self, message="language already exists in database."):
        current_app.logger.error("language already exists in database.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class notExistentLanguageError(usersException):
    def __init__(self, message="Language doesn't exists."):
        current_app.logger.error("Language doesn't exists.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)
