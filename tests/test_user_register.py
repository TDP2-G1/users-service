import json

from tests import INVALID_REGISTER, VALID_REGISTER
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
        print(data)
        self.assertEqual(data['id_user'], 1)
        self.assertEqual(status_code, 200)
