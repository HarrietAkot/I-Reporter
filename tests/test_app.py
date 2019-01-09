import unittest
import json
from api.views import app


class Testapp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = app.test_client(self)
        
    def test_index(self):
        resp = self.test_client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_create_red_flag(self):
        incident = {
            'created_by': 'Harriet',
            'incident_type': 'Corruption',
            'location': '23.3,33.6',
            'comment': 'Witnessed corruption in court',
            'images': 'image1.jpg',
            'videos': 'video1.mp4'
        }
        response = self.test_client.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'created redflag reccord!')


    def test_get_all_red_flags(self):
        resp = self.test_client.get(
            '/api/v1/red-flags/all' ,
             content_type='application/json'
            )
        self.assertEqual(resp.status_code, 200)


    def test_get_specific_red_flag(self):
        incident = {
            'created_by': 'Harriet',
            'incident_type': 'Corruption',
            'location': '23.3,33.6',
            'comment': 'Witnessed corruption in court',
            'images': 'image1.jpg',
            'videos': 'video1.mp4'
        }
        self.test_client.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident)
        )
        get_specific_red_flag = self.test_client.get(
            '/api/v1/red-flags/1',
            content_type='application/json'
        )
        self.assertEqual(get_specific_red_flag.status_code, 200)

    def test_edit_flag_location(self):
        incident = {
            'created_by': 'Harriet',
            'incident_type': 'Corruption',
            'location': '23.3,33.6',
            'comment': 'Witnessed corruption in court',
            'images': 'image1.jpg',
            'videos': 'video1.mp4'
        }
        self.test_client.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident)
        )
        new_location = {
            'location':'00.0,00.0'
        }

        edit_specific_red_flag_location = self.test_client.patch(
            '/api/v1/red-flags/1/location',
            content_type='application/json',
            data=json.dumps(new_location)
        )
        self.assertEqual(edit_specific_red_flag_location.status_code, 200)

    def test_edit_red_flag_comment(self):
        incident = {
            'created_by': 'Harriet',
            'incident_type': 'Corruption',
            'location': '23.3,33.6',
            'comment': 'Witnessed corruption in court',
            'images': 'image1.jpg',
            'videos': 'video1.mp4'
        }
        self.test_client.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident)
        )
        new_comment = {
            'location':'bribery'
        }

        edit_specific_red_flag_comment = self.test_client.patch(
            '/api/v1/red-flags/1/location',
            content_type='application/json',
            data=json.dumps(new_comment)
        )
        self.assertEqual(edit_specific_red_flag_comment.status_code, 200)

    def test_delete_red_flag(self):
        incident = {
            'created_by': 'Harriet',
            'incident_type': 'Corruption',
            'location': '23.3,33.6',
            'comment': 'Witnessed corruption in court',
            'images': 'image1.jpg',
            'videos': 'video1.mp4'
        }
        self.test_client.post(
            '/api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident)
        )
        delete = self.test_client.delete(
            '/api/v1/red-flags/1',
            content_type='application/json'
        )
        self.assertEqual(delete.status_code, 301)

if __name__ == '__main__':
    app.run(debug=True)