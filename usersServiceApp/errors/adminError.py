from flask import current_app
from usersServiceApp.errors.usersException import usersException


class loginAdminError(usersException):
    def __init__(self, message="E-mail and/or password incorrect."):
        current_app.logger.error("E-mail and/or password incorrect.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class registrationAdminError(usersException):
    def __init__(self, message="All fields must be completed."):
        current_app.logger.error("All fields must be completed.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class notExistentAdminError(usersException):
    def __init__(self, message="The user doesn't exists."):
        current_app.logger.error("The user doesn't exists.")
        self.message = message
        self.error_code = 404
        super().__init__(self.message, self.error_code)


class mailTakenAdminError(usersException):
    def __init__(self, message="The email for the registration is already taken."):
        current_app.logger.error("The email for the registration is already taken.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)
