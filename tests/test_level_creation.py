import json

from usersServiceApp import create_app
import unittest


def level_creation(tester, _level_descrip):
    response = tester.post("/level/", data=json.dumps({'level_description': _level_descrip}), content_type='application'
                                                                                                           '/json')
    return response


class FlaskTest(unittest.TestCase):

    def test_valid_level_creation(self):
        tester = create_app().test_client(self)
        response = level_creation(tester, 'Basic')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['level_description'], "Basic")
        self.assertEqual(status_code, 200)

    def test_invalid_level_creation_already_exists(self):
        tester = create_app().test_client(self)
        level_creation(tester, 'Basic')
        response = level_creation(tester, 'basic')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "level already exists in database.")
        self.assertEqual(status_code, 403)


    def test_valid_level_creation_get(self):
        tester = create_app().test_client(self)
        response = level_creation(tester, 'Basic')
        response = tester.get("/level/", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0]['id_level'], 1)
        self.assertEqual(data[0]['level_description'], "Basic")
        self.assertEqual(status_code, 200)
