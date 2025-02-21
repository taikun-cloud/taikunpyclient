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

from taikunpycore.models.notification_history import NotificationHistory

class TestNotificationHistory(unittest.TestCase):
    """NotificationHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationHistory:
        """Test NotificationHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationHistory`
        """
        model = NotificationHistory()
        if include_optional:
            return NotificationHistory(
                data = [
                    taikunpycore.models.notification_list_dto.NotificationListDto(
                        created_at = '', 
                        action_message = '', 
                        action_status = 'succeeded', 
                        username = '', 
                        category = 'StartAddServer', 
                        project_name = '', 
                        project_id = 56, 
                        is_deleted = True, )
                    ],
                total_count = 56
            )
        else:
            return NotificationHistory(
                data = [
                    taikunpycore.models.notification_list_dto.NotificationListDto(
                        created_at = '', 
                        action_message = '', 
                        action_status = 'succeeded', 
                        username = '', 
                        category = 'StartAddServer', 
                        project_name = '', 
                        project_id = 56, 
                        is_deleted = True, )
                    ],
                total_count = 56,
        )
        """

    def testNotificationHistory(self):
        """Test NotificationHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
