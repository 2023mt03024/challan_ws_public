from mockito import mock, verify
import unittest

from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()
    
    def tearDown(self):
        self.ctx.pop()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert 'View Challans' in response.get_data(as_text=True)

    def test_about(self):
        response = self.client.get("/about")
        assert response.status_code == 200
        assert 'Web application for viewing challans' in response.get_data(as_text=True)

    def test_generate_challan(self):
        response = self.client.post("/", 
                                    data=dict(vehicle_number='TS07HR9552'
                                               ))
        assert response.status_code == 302        
