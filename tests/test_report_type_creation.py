import json

from usersServiceApp import create_app
import unittest


def report_type_creation(tester, _report_type_descrip):
    response = tester.post("/report_type/", data=json.dumps({'report_type_description': _report_type_descrip}), content_type='application'
                                                                                                           '/json')
    return response


class FlaskTest(unittest.TestCase):

    def test_valid_report_type_creation(self):
        tester = create_app().test_client(self)
        response = report_type_creation(tester, 'Offensive')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['report_type_description'], "Offensive")
        self.assertEqual(status_code, 200)

    def test_invalid_report_type_creation_already_exists(self):
        tester = create_app().test_client(self)
        report_type_creation(tester, 'Offensive')
        response = report_type_creation(tester, 'Offensive')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], "ReportType already exists in database.")
        self.assertEqual(status_code, 403)


    def test_valid_report_type_creation_get(self):
        tester = create_app().test_client(self)
        response = report_type_creation(tester, 'Offensive')
        response = tester.get("/report_type/", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0]['id_report_type'], 1)
        self.assertEqual(data[0]['report_type_description'], "Offensive")
        self.assertEqual(status_code, 200)
