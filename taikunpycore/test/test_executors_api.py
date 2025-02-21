# coding: utf-8

"""
    Taikun - WebApi

    This Api will be responsible for overall data distribution and authorization.

    The version of the OpenAPI document: v1
    Contact: noreply@taikun.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from taikunpycore.api.executors_api import ExecutorsApi


class TestExecutorsApi(unittest.TestCase):
    """ExecutorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExecutorsApi()

    def tearDown(self) -> None:
        pass

    def test_executors_create(self) -> None:
        """Test case for executors_create

        Create an executor
        """
        pass

    def test_executors_delete(self) -> None:
        """Test case for executors_delete

        Delete an executor
        """
        pass

    def test_executors_edit_health(self) -> None:
        """Test case for executors_edit_health

        Update health status of the executor by Id
        """
        pass

    def test_executors_list(self) -> None:
        """Test case for executors_list

        Retrieve a list of kube configs of executors
        """
        pass

    def test_executors_toggle(self) -> None:
        """Test case for executors_toggle

        Toggle an executor
        """
        pass


if __name__ == '__main__':
    unittest.main()
