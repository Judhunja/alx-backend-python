#!/usr/bin/env python3
"""This module contains a class GithubOrgClient"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """Contains tests for github client"""

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    # Patch is done from the module where get_json is used(client)
    # and not from where is was implemented(utils)
    @patch("client.get_json")
    def test_org(self, value, mock_gjson):
        """Test github org client by google and abc"""
        mock_gjson.return_value = {}
        clientorg = GithubOrgClient(value)
        result = clientorg.org
        mock_gjson.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=value)
        )
        self.assertEqual(result, {})

    def test_public_repos(self):
        """Test that GitHubOrgClient._public_repos_url works properly"""
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_client_url:
            mock_client_url.return_value = {
                "repos_url":
                    "https://api.github.com/orgs/exampleorg/examplerepo"
            }
            result = client.GithubOrgClient._public_repos_url
            # using fget to retrieve the value of org property
            # ["repos_url"]. fget searches the org property
            # of client.GithubOrgClient
            result_val = result.fget(client.GithubOrgClient)
            expected_res = "https://api.github.com/orgs/exampleorg/examplerepo"
            self.assertEqual(result_val, expected_res)


if __name__ == "__main__":
    unittest.main()
