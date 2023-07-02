import unittest

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Pirate Family Game", response.data)

    def test_main_character_route(self):
        response = self.app.get("/main-character")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Create your main character", response.data)

    def test_create_main_character_route(self):
        data = {"name": "John", "email": "john@example.com"}
        response = self.app.post("/create-main-character", data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Choose Your Character", response.data)

    def test_choose_character_route(self):
        response = self.app.get("/characters")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Choose Your Character", response.data)

    def test_play_route(self):
        character_name = "Victor"
        response = self.app.get(f"/playwith/{character_name}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Victor", response.data)


if __name__ == "__main__":
    unittest.main()
