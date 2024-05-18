#!/usr/bin/env python3
"""This module contains a class GithubOrgClient"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
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


if __name__ == "__main__":
    unittest.main()
