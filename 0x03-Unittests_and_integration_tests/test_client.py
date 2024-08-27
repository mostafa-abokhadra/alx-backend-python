#!/usr/bin/env python3
"""test_client module
"""
import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized
# from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ testing some class
    """
    @parameterized.expand(["google", "abc"])
    # @patch('client.get_json')
    # def test_org(self, org: str, mock_get_json: MagicMock) -> None:
    #     """testing organization
    #     """
    #     res = {"name": "mostafa abokhadra"}
    #     mock_get_json.return_value = {"name": "mostafa abokhadra"}
    #     inst = GithubOrgClient(org)
    #     val = inst.org
    #     val = inst.org
    #     self.assertIsInstance(val, dict)
    #     self.assertEqual(val, res)
    #     mock_get_json.assert_called_once()
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
