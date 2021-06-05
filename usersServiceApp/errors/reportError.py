from flask import current_app
from usersServiceApp.errors.usersException import usersException


class existentReportTypeError(usersException):
    def __init__(self, message="ReportType already exists in database."):
        current_app.logger.error("ReportType already exists in database.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)


class notExistentReportTypeError(usersException):
    def __init__(self, message="ReportType doesn't exists."):
        current_app.logger.error("ReportType doesn't exists.")
        self.message = message
        self.error_code = 403
        super().__init__(self.message, self.error_code)