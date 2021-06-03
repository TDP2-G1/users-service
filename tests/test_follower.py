import json

from tests import VALID_REGISTER, INVALID_MINOR_REGISTER, INVALID_REGISTER_DATE_FORMAT, ANOTHER_VALID_REGISTER, \
    VALID_FOLLOWER
from tests.test_genre_creation import genre_creation
from tests.test_language_creation import language_creation
from tests.test_level_creation import level_creation
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_valid_follower(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/follower/", data=VALID_FOLLOWER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_1'], 2)
        self.assertEqual(status_code, 200)


    def test_invalid_follower_not_existent_users(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/follower/", data=VALID_FOLLOWER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], 'User ID does not exist.')
        self.assertEqual(status_code, 404)


    def test_valid_follower_get(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/follower/", data=VALID_FOLLOWER, content_type='application/json')
        response = tester.get("/follower/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0], 2)
        self.assertEqual(status_code, 200)
        response = tester.get("/follower/2", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0], 1)
        self.assertEqual(status_code, 200)
