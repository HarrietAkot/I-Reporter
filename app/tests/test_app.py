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

    def test_create_red_flag(self):
        resp = self.client.post('/api/v1/red-flags')
        self.assertEqual(resp.status_code, 200)
		result = client_tester().post('/', content_type='application/json',
                           data=json.dumps({"createdBy" : "Noah",
                                            "title":"Judicial corruption",
                                            "location" : [0.8789, 9.5672],
                                            "comment" : "Bribery"}))
    assert result.status_code == 201

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['status'] == 201
    assert json_data['data'][0]['message'] == "Created red-flag record"
		

    def test_get_all_red_flags(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
		result = client_tester().get('/api/v1/red-flags/all')
		assert result.status_code == 200
		data = json.loads(result.data)
		assert data['data'][0]['flag_id'] == 1
		assert data['data'][0]['incident_type'] == "corruption"
		assert data['data'][0]['location'] == [0.8789,9.5672]
		assert data['data'][0]['created_by'] == "Noah"
		assert data['data'][0]['comments'] == "corruption"
		assert data['data'][0]['status'] == "draft"

    def test_get_specific_red_flag(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
		
		result = client_tester().get('/api/v1/red-flags/1')
		assert result.status_code == 200
		json_data = json.loads(result.data)
		assert json_data['data'][0]['id'] == 1
		assert json_data['data'][0]['title'] == "Judicial corruption"
		assert json_data['data'][0]['location'] == [0.8789,9.5672]
		assert json_data['data'][0]['createdBy'] == "Noah"
		assert json_data['data'][0]['comment'] == "Bribery"
		assert json_data['data'][0]['status'] == "draft"

    def test_edit_flag_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
		
		result = client_tester().put('api/v1/red-flags/1/location',content_type='application/json',
                           data=json.dumps({"location" : [10.1010,20.2020]}))
    
    assert result.status_code == 200

    json_data = json.loads(result.data)
    assert "data" in json_data
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['message'] == "Updated red-flag record’s location"

    #make a put request to check whether the red-flag has been updated
    check_redflag = client_tester().get('/api/v1/red-flags/1')
    assert check_redflag.status_code == 200
    json_data = json.loads(check_redflag.data)
    assert json_data['data'][0]['id'] == 1
    assert json_data['data'][0]['title'] == "Judicial corruption"
    assert json_data['data'][0]['location'] == [10.1010,20.2020]
    assert json_data['data'][0]['createdBy'] == "Noah"
    assert json_data['data'][0]['comment'] == "Bribery"
    assert json_data['data'][0]['status'] == "draft"

    def test_edit_red_flag_comment(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_delete_red_flag(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

