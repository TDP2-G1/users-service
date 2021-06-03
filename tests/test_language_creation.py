import json

from usersServiceApp import create_app
import unittest


def language_creation(tester, _language_descrip):
    response = tester.post("/language/", data=json.dumps({'language_description': _language_descrip}), content_type='application'
                                                                                                           '/json')
    return response


class FlaskTest(unittest.TestCase):

    def test_valid_language_creation(self):
        tester = create_app().test_client(self)
        response = language_creation(tester, 'Spanish')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['language_description'], "Spanish")
        self.assertEqual(status_code, 200)

    def test_invalid_language_creation_already_exists(self):
        tester = create_app().test_client(self)
        language_creation(tester, 'Spanish')
        response = language_creation(tester, 'spanish')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "language already exists in database.")
        self.assertEqual(status_code, 403)


    def test_valid_language_creation(self):
        tester = create_app().test_client(self)
        response = language_creation(tester, 'Spanish')
        status_code = response.status_code
        response = tester.get("/language/", content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0]['id_language'], 1)
        self.assertEqual(data[0]['language_description'], "Spanish")
        self.assertEqual(status_code, 200)
