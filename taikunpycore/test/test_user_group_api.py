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

from taikunpycore.api.user_group_api import UserGroupApi


class TestUserGroupApi(unittest.TestCase):
    """UserGroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserGroupApi()

    def tearDown(self) -> None:
        pass

    def test_projectgroups_unbind_project_group(self) -> None:
        """Test case for projectgroups_unbind_project_group

        Unbind project group from user group
        """
        pass

    def test_usergroups_bind_projects_group(self) -> None:
        """Test case for usergroups_bind_projects_group

        Bind project groups
        """
        pass

    def test_usergroups_bind_user(self) -> None:
        """Test case for usergroups_bind_user

        Bind Users to group
        """
        pass

    def test_usergroups_create(self) -> None:
        """Test case for usergroups_create

        Add user groups
        """
        pass

    def test_usergroups_delete(self) -> None:
        """Test case for usergroups_delete

        Remove user group(s)
        """
        pass

    def test_usergroups_list(self) -> None:
        """Test case for usergroups_list

        Retrieve list of user groups
        """
        pass

    def test_usergroups_list_by_project_group_id(self) -> None:
        """Test case for usergroups_list_by_project_group_id

        Dropdown list
        """
        pass

    def test_usergroups_unbind_user(self) -> None:
        """Test case for usergroups_unbind_user

        Unbind Users from group
        """
        pass

    def test_usergroups_update(self) -> None:
        """Test case for usergroups_update

        Update user groups
        """
        pass

    def test_usergroups_user_group_users(self) -> None:
        """Test case for usergroups_user_group_users

        Retrieve list of users by user group id
        """
        pass


if __name__ == '__main__':
    unittest.main()
