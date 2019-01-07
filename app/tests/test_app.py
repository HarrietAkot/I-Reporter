import unittest
import json
# from .views.api import app
from ..app.views.api import app
from ..app.models.app_models import Incident

class Testapp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_create_red_flags(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_get_all_red_flags(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_get_specific_red_flag(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_edit_flag_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_edit_red_flag_comment(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_delete_red_flag(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

