import json

from tests import VALID_REGISTER, INVALID_MINOR_REGISTER, INVALID_REGISTER_DATE_FORMAT, ANOTHER_VALID_REGISTER, \
    VALID_FOLLOWER, VALID_BLOCK, VALID_UNBLOCK
from tests.test_genre_creation import genre_creation
from tests.test_language_creation import language_creation
from tests.test_level_creation import level_creation
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_valid_block(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/block/", data=VALID_BLOCK, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id_1'], 2)
        self.assertEqual(status_code, 200)


    def test_invalid_block_not_existent_users(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/block/", data=VALID_BLOCK, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], 'User ID does not exist.')
        self.assertEqual(status_code, 404)


    def test_valid_block_get(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/block/", data=VALID_BLOCK, content_type='application/json')
        response = tester.get("/block/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['blocked'][0]['id_user'], 2)
        self.assertEqual(status_code, 200)
        response = tester.get("/block/2", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['blocked_by'][0]['id_user'], 1)
        self.assertEqual(status_code, 200)
        response = tester.get("/user/", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)


    def test_valid_unblock(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        tester.post("/block/", data=VALID_BLOCK, content_type='application/json')
        response = tester.get("/block/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['blocked'][0]['id_user'], 2)
        self.assertEqual(status_code, 200)
        response = tester.get("/block/2", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['blocked_by'][0]['id_user'], 1)
        self.assertEqual(status_code, 200)
        response = tester.get("/user/", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        tester.post("/block/", data=VALID_UNBLOCK, content_type='application/json')
        response = tester.get("/block/2", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(status_code, 200)
        self.assertEqual(data['blocked_by'], [])

    def test_invalid_unblock(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        tester.post("/block/", data=VALID_BLOCK, content_type='application/json')
        response = tester.get("/block/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['blocked'][0]['id_user'], 2)
        self.assertEqual(status_code, 200)
        response = tester.get("/block/2", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['blocked_by'][0]['id_user'], 1)
        self.assertEqual(status_code, 200)
        response = tester.get("/user/", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)
        tester.post("/block/", data=VALID_BLOCK, content_type='application/json')
        response = tester.get("/block/2", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(status_code, 200)

