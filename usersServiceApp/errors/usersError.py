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


class FBUserAlreadyRegisteredError(usersException):
    def __init__(self, message="FB User Already Registered"):
        current_app.logger.error("FB User Already Registered")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class FBUserNotRegisteredError(usersException):
    def __init__(self, message="User is not registered."):
        current_app.logger.error("User is not registered.")
        self.message = message
        self.error_code = 404
        super().__init__(self.message, self.error_code)


class DateFormatError(usersException):
    def __init__(self, message="DATE Format must be dd/mm/YYYY."):
        current_app.logger.error("DATE Format must be dd/mm/YYYY.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class UserNotExistsError(usersException):
    def __init__(self, message="User ID does not exist."):
        current_app.logger.error("User ID does not exist.")
        self.message = message
        self.error_code = 404
        super().__init__(self.message, self.error_code)


class UserDisabledError(usersException):
    def __init__(self, message="User is disabled."):
        current_app.logger.error("User is disabled.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class EmptyUserStatusError(usersException):
    def __init__(self, message="User status can't be empty."):
        current_app.logger.error("User status can't be empty.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)