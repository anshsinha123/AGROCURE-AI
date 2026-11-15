import unittest
from unittest.mock import patch

from fastapi import HTTPException

from backend import app_server


class LoginSecurityTests(unittest.TestCase):
    def test_demo_email_cannot_authenticate_as_another_user(self):
        stored_users = [
            {
                "id": "usr_registered",
                "email": "registered@example.com",
                "password_hash": "not-a-matching-hash",
            }
        ]
        request = app_server.LoginRequest(
            email="farmer@agrocure.ai",
            password="incorrect-password",
        )

        with patch.object(app_server, "load_json", return_value=stored_users):
            with self.assertRaises(HTTPException) as error:
                app_server.login(request)

        self.assertEqual(error.exception.status_code, 401)
