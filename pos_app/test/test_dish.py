import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"]="testing"

class TestDish(unittest.TestCase):
    def setUp(self):
        "This function runs before each test to prepare for them"
        # create app instance to test
        self.app = create_app()
        # the test_client function generates an imaginary browser that can make requests
        self.client = self.app.test_client()
    
    def test_dish_menu(self):
        "Use the client to make a request"
        response = self.client.get("/dishes/")
        data = response.get_json()

         # Now to perform tests on the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Menu</h1>', response.data)

    def test_create_bad_dish(self):
        response = self.client.post("/dishes/", data={"dish_name": ""})
        self.assertEqual(response.status_code, 400)

    def test_create_good_dish(self):
        response = self.client.post("/dishes/", data={"dish_name": "testdish"})
        self.assertEqual(response.status_code, 302)
        self.client.post(f"/dishes/{response.get_json()['dish_id']}/delete/")

    def test_delete_dish(self):
        response1 = self.client.post("/dishes/", data={"dish_name": "testdish"})
        id = response1.get_json()["dish_id"]
        
        response2 = self.client.post(f"/dishes/{id}/delete/")
        self.assertEqual(response2.status_code, 200)

    def test_update_dish(self):
        # create the resource to test
        response1 = self.client.post("/dishes/", data={"dish_name": "testdish"})
        id = response1.get_json()["dish_id"]

        # change the resource and check the changes were successful
        response2 = self.client.put(f"/dishes/{id}/", json={"dish_name": "newtestdish"})
        self.assertEqual(response2.status_code, 302)
        data = response2.get_json()
        self.assertEqual(data["dish_name"], "newtestdish")

        # clean up the resource afterwards
        self.client.post(f"/dishes/{id}/delete/")