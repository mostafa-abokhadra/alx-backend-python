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
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json: MagicMock) -> None:
        """testing organization
        """
        res = {"name": "mostafa abokhadra"}
        mock_get_json.return_value = {"name": "mostafa abokhadra"}
        inst = GithubOrgClient(org)
        val = inst.org
        val = inst.org
        self.assertIsInstance(val, dict)
        self.assertEqual(val, res)
        mock_get_json.assert_called_once()
    # @parameterized.expand([
    #     ("google", {'login': "google"}),
    #     ("abc", {'login': "abc"}),
    # ])
    # @patch(
    #     "client.get_json",
    # )
    # def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
    #     """Tests the `org` method."""
    #     mocked_fxn.return_value = MagicMock(return_value=resp)
    #     gh_org_client = GithubOrgClient(org)
    #     self.assertEqual(gh_org_client.org(), resp)
    #     mocked_fxn.assert_called_once_with(
    #         "https://api.github.com/orgs/{}".format(org)
    #     )

    # @parameterized.expand([""])
    @patch("client.GithubOrgClient.org")
    def test_public_repos_url(self, mock_org):
        """ test_buplic_repos_url doc
        """
        res = {"repos_url": "https://url.com"}
        mock_org.return_value = res
        inst = GithubOrgClient("google")
        self.assertEqual(inst.org()['repos_url'], res["repos_url"])
        # print(inst._public_repos_url)
        # print(mock_org.return_value)
        # print(res)
        # with patch.object(GithubOrgClient, "org", return_value=res) as mock_org:
            # val = GithubOrgClient._public_repos_url
            # print(val)
            # print(mock_org.return_value)
            # print("$" * 40)
            # self.assertEqual(mock_org.return_value, val)  
