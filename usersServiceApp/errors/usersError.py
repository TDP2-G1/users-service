from flask import current_app
from usersServiceApp.errors.usersException import usersException


class DataBaseError(usersException):
    def __init__(self, message="Something happened while creating in the database."):
        current_app.logger.error("Something happened while creating in the database.")
        self.message = message
        self.error_code = 500
        super().__init__(self.message, self.error_code)


class AgeUnder16Error(usersException):
    def __init__(self, message="Age must be at least 16."):
        current_app.logger.error("Age must be at least 16.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)
