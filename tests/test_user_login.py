import json

from tests import VALID_REGISTER, INVALID_MINOR_REGISTER, INVALID_REGISTER_DATE_FORMAT, VALID_DISABLED_ACCOUNT
from tests.test_genre_creation import genre_creation
from tests.test_language_creation import language_creation
from tests.test_level_creation import level_creation
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_valid_user_login(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_invalid_user_login_disabled(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)
        response = tester.put("/user/1/account_status", data=VALID_DISABLED_ACCOUNT, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 403)
        self.assertEqual(data['Error'], 'User is disabled.')
