import json, unittest
from app import create_app
from app.extensions import db

class MechanicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def test_create_and_get_mechanic(self):
        res = self.client.post('/mechanics/', json={'name':'Sam','specialization':'Engine'})
        self.assertEqual(res.status_code, 201)
        mech_id = res.get_json()['id']
        res = self.client.get('/mechanics/')
        data = res.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], mech_id)

    def test_update_mechanic(self):
        res = self.client.post('/mechanics/', json={'name':'Alex','specialization':'Brakes'})
        mech_id = res.get_json()['id']
        res = self.client.put(f'/mechanics/{mech_id}', json={'specialization':'Tires'})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['specialization'], 'Tires')

    def test_delete_mechanic(self):
        mech_id = self.client.post('/mechanics/', json={'name':'Kim','specialization':'Suspension'}).get_json()['id']
        res = self.client.delete(f'/mechanics/{mech_id}')
        self.assertEqual(res.status_code, 204)
        res = self.client.get('/mechanics/')
        self.assertEqual(res.get_json(), [])
