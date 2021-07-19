import json

from tests import VALID_REGISTER, ANOTHER_VALID_REGISTER, VALID_REPORT, VALID_OTHER_REPORT, VALID_UPDATE_REPORT_FALSE, \
    VALID_UPDATE_REPORT_TRUE, VALID_OTHER_REPORT_2
from tests.test_genre_creation import genre_creation
from tests.test_language_creation import language_creation
from tests.test_level_creation import level_creation
from usersServiceApp import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def test_valid_report(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/report/", data=VALID_REPORT, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Status'], 'Report Created')
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data['reported_by'][0], 2)
        self.assertEqual(status_code, 200)

    def test_invalid_report_not_existent_users(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/report/", data=VALID_REPORT, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Error'], 'User ID does not exist.')
        self.assertEqual(status_code, 404)

    def test_valid_report_get(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/report/", data=VALID_REPORT, content_type='application/json')
        response = tester.get("/report/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0]['id_report'], 1)
        self.assertEqual(status_code, 200)

    def test_valid_other_text_report_get(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/report/", data=VALID_OTHER_REPORT, content_type='application/json')
        response = tester.get("/report/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data[0]['id_report'], 1)
        self.assertEqual(data[0]['text'], "Cosas feas")
        self.assertEqual(status_code, 200)


    def test_valid_update_report(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/report/", data=VALID_OTHER_REPORT, content_type='application/json')
        response = tester.get("/report/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data[0]['id_report'], 1)
        self.assertEqual(data[0]['is_pending'], True)
        self.assertEqual(status_code, 200)
        response = tester.put("/report/1", data=VALID_UPDATE_REPORT_FALSE, content_type='application/json')
        response = tester.get("/report/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data[0]['id_report'], 1)
        self.assertEqual(data[0]['is_pending'], False)
        self.assertEqual(status_code, 200)
        response = tester.put("/report/1", data=VALID_UPDATE_REPORT_TRUE, content_type='application/json')
        response = tester.get("/report/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data[0]['id_report'], 1)
        self.assertEqual(data[0]['is_pending'], True)
        self.assertEqual(status_code, 200)
        response = tester.put("/report/1", data=VALID_UPDATE_REPORT_FALSE, content_type='application/json')
        response = tester.get("/report/1", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data[0]['id_report'], 1)
        self.assertEqual(data[0]['is_pending'], False)
        self.assertEqual(status_code, 200)

    def test_valid_dataset(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/report/", data=VALID_OTHER_REPORT, content_type='application/json')
        response = tester.get("/report/dataset", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data[0]['abiertas'], 1)
        self.assertEqual(data[0]['pendientes'], 1)
        self.assertEqual(status_code, 200)
        response = tester.post("/report/", data=VALID_OTHER_REPORT_2, content_type='application/json')
        response = tester.put("/report/1", data=VALID_UPDATE_REPORT_FALSE, content_type='application/json')
        response = tester.get("/report/dataset", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data[0]['abiertas'], 2)
        self.assertEqual(data[0]['pendientes'], 1)
        self.assertEqual(status_code, 200)

    def test_valid_report_with_status(self):
        tester = create_app().test_client(self)
        genre_creation(tester, 'Male')
        language_creation(tester, 'English')
        level_creation(tester, 'Advanced')
        tester.post("/report_type/", data=json.dumps({'report_type_description': 'Algo malo'}),
                    content_type='application'
                                 '/json')
        response = tester.post("/user/", data=VALID_REGISTER, content_type='application/json')
        response = tester.post("/user/", data=ANOTHER_VALID_REGISTER, content_type='application/json')
        response = tester.post("/report/", data=VALID_REPORT, content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Status'], 'Report Created')
        self.assertEqual(status_code, 200)
        response = tester.get("/user/u23y48298", content_type='application/json')
        status_code = response.status_code
        data = json.loads(response.get_data(as_text=True))
        print(data)
        self.assertEqual(data['reported_by'][0], 2)
        self.assertEqual(data['reported_by_with_status'][0]['is_pending'], True)
        self.assertEqual(data['reported_by_with_status'][0]['user_reported_by'], 2)
        self.assertEqual(status_code, 200)
