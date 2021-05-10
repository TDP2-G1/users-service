import json

from usersServiceApp import create_app
import unittest


def genre_creation(tester, _genre_descrip):
    response = tester.post("/genre/", data=json.dumps({'genre_description': _genre_descrip}), content_type='application'
                                                                                                           '/json')
    return response


class FlaskTest(unittest.TestCase):

    def test_valid_genre_creation(self):
        tester = create_app().test_client(self)
        response = genre_creation(tester, 'Female')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['genre_description'], "Female")
        self.assertEqual(status_code, 200)

    def test_invalid_genre_creation_already_exists(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Female')
        response = genre_creation(tester, 'female')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "Genre already exists in database.")
        self.assertEqual(status_code, 403)
