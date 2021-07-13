import json

from tests import VALID_REGISTER, INVALID_MINOR_REGISTER, INVALID_REGISTER_DATE_FORMAT, VALID_DISABLED_ACCOUNT, \
    VALID_LOGIN_1, VALID_LOGIN_2, ANOTHER_VALID_REGISTER
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


    def test_valid_user_login_with_log_dataset(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/login/", data=VALID_LOGIN_1, content_type='application/json')
        response = tester.post("/login/", data=VALID_LOGIN_1, content_type='application/json')
        response = tester.post("/login/", data=VALID_LOGIN_2, content_type='application/json')
        response = tester.post("/login/", data=VALID_LOGIN_2, content_type='application/json')
        response = tester.get("/login/dataset", content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(data[0]['active_users'], 2)
