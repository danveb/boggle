from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setup(self):
        self.client = app.test_client()
        app.config['TESTING'] = True 

    def test_route(self):
        with app.test_client() as client:
            index = client.get('/')
            indexhtml = index.get_data(as_text=True)
            self.assertIn('<h1>Flask Boggle</h1>', indexhtml)
            self.assertEqual(index.status_code, 200)
    
    def test_word_check(self):
        with app.test_client() as client:
            response = client.get("/check", data={"word": "jump"})
            self.assertEqual(response.status_code, 200)
    
    # def test_score(self):
    #     with app.test_client() as client:
    #         response = client.post('/score', data={'score': 4})
    #         self.assertEqual(response.status_code, 200)

        

