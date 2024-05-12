#!/usr/bin/env python3
"""This module contains a class TestAccessNestedMap"""

import unittest
from unittest.mock import patch
import requests
import utils
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests the nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Checks whether the path specified matches
        the actual path of the nested map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """Checks for Keyerror raised by the function of the wrong path
        is specified for the nested map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests that the the get_json method returns a valid
    json object for the given url"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, return_val):
        """Tests that the output of get_json is equal to the output
        in the parameterized.expand tuple"""
        with patch.object(
            utils, "get_json", return_value=return_val
        ) as mock_get:
            result = utils.get_json(url)
            mock_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
