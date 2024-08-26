#!/usr/bin/env python3
"""testing access_nested_map module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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
    def test_get_json(self, url, payload, mock_get):
        """testing http requests
        """
        res = Mock()
        res.json.return_value = payload
        mock_get.return_value = res
        self.assertEqual(get_json(url), payload)
        mock_get.assert_called_with(url)


class TestMemoize(unittest.TestCase):
    """test memoize class
    """
    # @patch.object(__name__ + '.TestClass', "a_method")
    def test_memoize(self):

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            mock_method.return_value = 42
            obj = TestClass()
            obj.a_property
            obj.a_property
            mock_method.assert_called_once()
