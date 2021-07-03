import json

from tests import VALID_REGISTER, INVALID_MINOR_REGISTER, INVALID_REGISTER_DATE_FORMAT, VALID_DISABLED_ACCOUNT, \
    INVALID_USER_STATUS_1, INVALID_USER_STATUS_2, VALID_USER_STATUS_1, VALID_USER_STATUS_2, VALID_USER_STATUS_3
from tests.test_genre_creation import genre_creation
from tests.test_language_creation import language_creation
from tests.test_level_creation import level_creation
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_user_status_online_after_register(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)
        print(data)
        self.assertEqual(data['user_status'], 'online')
        # response = tester.put("/user/1/account_status", data=VALID_DISABLED_ACCOUNT, content_type='application/json')
        # status_code = response.status_code
        # data = json.loads(response.get_data(as_text=True))
        # self.assertEqual(status_code, 200)

    def test_user_status_invalid_empty(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)
        self.assertEqual(data['user_status'], 'online')
        response = tester.put("/user/1/user_status", data=INVALID_USER_STATUS_1, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 403)
        self.assertEqual(data['Error'], "User status can't be empty.")
        response = tester.put("/user/1/user_status", data=INVALID_USER_STATUS_2, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 403)
        self.assertEqual(data['Error'], "User status can't be empty.")

    def test_user_status_valid_change(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)
        self.assertEqual(data['user_status'], 'online')
        response = tester.put("/user/1/user_status", data=VALID_USER_STATUS_1, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        self.assertEqual(data['user_status'], 'busy')
        response = tester.put("/user/1/user_status", data=VALID_USER_STATUS_2, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        self.assertEqual(data['user_status'], 'offline')
        response = tester.put("/user/1/user_status", data=VALID_USER_STATUS_3, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        self.assertEqual(data['user_status'], 'online')
