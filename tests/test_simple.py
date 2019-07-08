from app import app
import unittest
import os
from spotter import T_NON_NUM, T_LEFT_MOST

class TestSimpleSpotter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        app.testing = True

    def tearDown(self):
        pass

    def test_left_most_0(self):
        fname = "sample_col_0.csv"
        fdir = os.path.join("tests", fname)
        f = open(fdir)
        data = {'technique': T_LEFT_MOST, 'callback': ""}
        data['table'] = (f, "sample.csv")
        result = self.app.post('/spot', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 200, msg=result.data)
        self.assertTrue(result.is_json)
        j = result.get_json()
        self.assertEqual(j["subject_col_id"], 0)

    def test_left_most_1(self):
        fname = "sample_col_1.csv"
        fdir = os.path.join("tests", fname)
        f = open(fdir)
        data = {'technique': T_LEFT_MOST, 'callback': ""}
        data['table'] = (f, "sample.csv")
        result = self.app.post('/spot', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 200, msg=result.data)
        self.assertTrue(result.is_json)
        j = result.get_json()
        self.assertEqual(j["subject_col_id"], 0)

    def test_left_most_no(self):
        fname = "sample_col_no.csv"
        fdir = os.path.join("tests", fname)
        f = open(fdir)
        data = {'technique': T_LEFT_MOST, 'callback': ""}
        data['table'] = (f, "sample.csv")
        result = self.app.post('/spot', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 200, msg=result.data)
        self.assertTrue(result.is_json)
        j = result.get_json()
        self.assertEqual(j["subject_col_id"], 0)

    def test_non_num_0(self):
        fname = "sample_col_0.csv"
        fdir = os.path.join("tests", fname)
        f = open(fdir)
        data = {'technique': T_NON_NUM, 'callback': ""}
        data['table'] = (f, "sample.csv")
        result = self.app.post('/spot', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 200, msg=result.data)
        self.assertTrue(result.is_json)
        j = result.get_json()
        self.assertEqual(j["subject_col_id"], 0)

    def test_non_num_1(self):
        fname = "sample_col_1.csv"
        fdir = os.path.join("tests", fname)
        f = open(fdir)
        data = {'technique': T_NON_NUM, 'callback': ""}
        data['table'] = (f, "sample.csv")
        result = self.app.post('/spot', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 200, msg=result.data)
        self.assertTrue(result.is_json)
        j = result.get_json()
        self.assertEqual(j["subject_col_id"], 1)

    def test_non_num_no(self):
        fname = "sample_col_no.csv"
        fdir = os.path.join("tests", fname)
        f = open(fdir)
        data = {'technique': T_NON_NUM, 'callback': ""}
        data['table'] = (f, "sample.csv")
        result = self.app.post('/spot', data=data, content_type='multipart/form-data')
        self.assertEqual(result.status_code, 200, msg=result.data)
        self.assertTrue(result.is_json)
        j = result.get_json()
        self.assertEqual(j["subject_col_id"], -1)


if __name__ == '__main__':
    unittest.main()
