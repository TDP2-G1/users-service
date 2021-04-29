import json

from tests import INVALID_REGISTER
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_invalid_genre_fail_register(self):
        tester = create_app().test_client(self)
        response = tester.post("/user/", data=INVALID_REGISTER, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "Something happened while creating in the database.")
        self.assertEqual(status_code, 500)
