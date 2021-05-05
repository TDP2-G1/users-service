import json

from tests import VALID_REGISTER, INVALID_MINOR_REGISTER, INVALID_REGISTER_DATE_FORMAT
from tests.test_genre_creation import genre_creation
from tests.test_language_creation import language_creation
from tests.test_level_creation import level_creation
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_valid_user_register(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)

    def test_invalid_user_register_invalid_genre(self):
        tester = create_app().test_client(self)
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data['Error'], "Genre doesn't exists.")
        self.assertEqual(status_code, 403)


    def test_invalid_user_register_invalid_language(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "Language doesn't exists.")
        self.assertEqual(status_code, 403)


    def test_invalid_user_register_invalid_level(self):
        tester = create_app().test_client(self)
        language_creation(tester, 'English')
        genre_creation(tester, 'Male')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "Level doesn't exists.")
        self.assertEqual(status_code, 403)


    def test_invalid_user_register_under_age(self):
        tester = create_app().test_client(self)
        language_creation(tester, 'English')
        genre_creation(tester, 'Male')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=INVALID_MINOR_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "Age must be at least 16.")
        self.assertEqual(status_code, 403)


    def test_invalid_user_register_date_format(self):
        tester = create_app().test_client(self)
        language_creation(tester, 'English')
        genre_creation(tester, 'Male')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=INVALID_REGISTER_DATE_FORMAT, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "DATE Format must be dd/mm/YYYY.")
        self.assertEqual(status_code, 403)
