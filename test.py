import unittest
from flask import Flask
from flask.testing import FlaskClient

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Pirate Family Game", response.data)

    def test_main_character_route(self):
        response = self.app.get("/main-character")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create Your Main Character", response.data)

    def test_create_main_character_route(self):
        data = {"name": "John Doe", "email": "johndoe@example.com"}
        response = self.app.post("/create-main-character", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "http://localhost/choose-character")

    def test_choose_character_route(self):
        response = self.app.get("/characters")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Choose Your Character", response.data)

    def test_play_route(self):
        character_name = "Victor"
        response = self.app.get(f"/playwith/{character_name}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"<h1>Play with {character_name}</h1>".encode(), response.data)


if __name__ == "__main__":
    unittest.main()
