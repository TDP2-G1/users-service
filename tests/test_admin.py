import json

from tests import VALID_ADMIN_REGISTER, VALID_ADMIN_LOGIN, INVALID_ADMIN_LOGIN, INVALID_ADMIN_REGISTER
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_valid_user_register(self):
        tester = create_app().test_client(self)
        response = tester.post("/admin/", data=VALID_ADMIN_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data['token'])
        self.assertEqual(status_code, 200)

    def test_invalid_user_register(self):
        tester = create_app().test_client(self)
        response = tester.post("/admin/", data=INVALID_ADMIN_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "All fields must be completed.")
        self.assertEqual(status_code, 403)

    def test_invalid_user_register_email_taken(self):
        tester = create_app().test_client(self)
        tester.post("/admin/", data=VALID_ADMIN_REGISTER, content_type='application/json')
        response = tester.post("/admin/", data=VALID_ADMIN_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "The email for the registration is already taken.")
        self.assertEqual(status_code, 403)

    def test_valid_user_login(self):
        tester = create_app().test_client(self)
        tester.post("/admin/", data=VALID_ADMIN_REGISTER, content_type='application/json')
        response = tester.post("/admin/login", data=VALID_ADMIN_LOGIN, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data['token'])
        self.assertEqual(status_code, 200)

    def test_invalid_user_login_not_exists_admin(self):
        tester = create_app().test_client(self)
        response = tester.post("/admin/login", data=VALID_ADMIN_LOGIN, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "The user doesn't exists.")
        self.assertEqual(status_code, 404)

    def test_invalid_user_login_invalid_password(self):
        tester = create_app().test_client(self)
        tester.post("/admin/", data=VALID_ADMIN_REGISTER, content_type='application/json')
        response = tester.post("/admin/login", data=INVALID_ADMIN_LOGIN, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "E-mail and/or password incorrect.")
        self.assertEqual(status_code, 403)
