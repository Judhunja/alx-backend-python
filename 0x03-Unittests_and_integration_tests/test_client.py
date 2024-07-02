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

    def test_public_repos_url(self):
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

    @patch('client.get_json')
    def test_public_repos(self, mock_gjson):
        """Test GithubOrgClient.public_repos returns the correct
        list of repos"""
        mock_gjson.return_value = [{"name": "test_url"}]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = 'test_url'
            res = GithubOrgClient('test_org')
            expected_val = ['test_url']
            result = res.public_repos()
            self.assertEqual(result, expected_val)

            mock_gjson.assert_called_once()
            mock_repos_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()
