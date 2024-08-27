#!/usr/bin/env python3
"""test_client module
"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ testing some class
    """
    @parameterized.expand(
            [
                "google",
                "google"
            ]
    )
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """testing organization
        """
        mock_get_json.return_value = {"name": "mostafa abokhadra"}
        inst = GithubOrgClient(org)
        val = inst.org
        val = inst.org
        self.assertIsInstance(val, dict)
        mock_get_json.assert_called_once()
