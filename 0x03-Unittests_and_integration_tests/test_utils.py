#!/usr/bin/env python3
"""Unit test for utils"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


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
        self.assertEqual(access_nested_map(input_map, path), expected)
