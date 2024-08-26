#!/usr/bin/env python3
"""testing access_nested_map module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json

class TestAccessNestedMap(unittest.TestCase):
    """ testing access_nested_map_class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, result):
        """testing ..."""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand(
        [
            ({}, ("a", )),
            ({"a": 1}, ("a", "b"))
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        self.assertRaises(KeyError, access_nested_map, nested_map, path)

class TestGetJson(unittest.TestCase):
    """testing get json
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, url, payload):
        """testing http requests
        """
