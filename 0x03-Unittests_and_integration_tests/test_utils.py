#!/usr/bin/env python3
"""Unit test for utils"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
        This a class for test access nested map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, input_map, path, expected) -> None:
        """test access """
        self.assertEqual(access_nested_map(input_map, path), expected)

    @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, input_map, path, error):
        """test exception"""
        with self.assertRaises(error):
            self.assertEqual(access_nested_map(input_map, path))


class TestGetJson(unittest.TestCase):
    """
        test get json
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_data):
        """test get json"""
        mock_json = Mock(return_value=test_payload)
        mock_data.return_value.json = mock_json
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_data.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test mempize Class"""

    def test_memoize(self):
        """Test memoize"""

        class TestClass:
            """Test class"""
            def a_method(self):
                """document"""
                return 42

            @memoize
            def a_property(self):
                """document"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_a_method:
            mock_a_method.return_value = 10

            instance_of_test_class = TestClass()
            res = instance_of_test_class.a_property
            self.assertEqual(instance_of_test_class.a_property, res)
            mock_a_method.assert_called_once()
