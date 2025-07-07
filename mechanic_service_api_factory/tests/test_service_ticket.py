import unittest
from app import create_app
from app.extensions import db

class TicketTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            # create mechanic
            self.mech_id = self.client.post('/mechanics/', json={'name':'Lee','specialization':'Diagnostics'}).get_json()['id']

    def test_create_ticket(self):
        res = self.client.post('/service-tickets/', json={'description':'Noise', 'customer_name':'Alice'})
        self.assertEqual(res.status_code, 201)
        ticket_id = res.get_json()['id']
        # assign mechanic
        res = self.client.put(f'/service-tickets/{ticket_id}/assign-mechanic/{self.mech_id}')
        self.assertEqual(res.status_code, 200)
        self.assertIn(self.mech_id, res.get_json()['mechanics'])
        # remove mechanic
        res = self.client.put(f'/service-tickets/{ticket_id}/remove-mechanic/{self.mech_id}')
        self.assertEqual(res.status_code, 200)
        self.assertNotIn(self.mech_id, res.get_json()['mechanics'])
        # list tickets
        res = self.client.get('/service-tickets/')
        self.assertEqual(len(res.get_json()), 1)
