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

from taikunpycore.models.alert_data import AlertData

class TestAlertData(unittest.TestCase):
    """AlertData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertData:
        """Test AlertData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertData`
        """
        model = AlertData()
        if include_optional:
            return AlertData(
                groups = [
                    taikunpycore.models.group.Group(
                        name = '', 
                        file = '', 
                        rules = [
                            taikunpycore.models.rule.Rule(
                                state = '', 
                                name = '', 
                                query = '', 
                                duration = 56, 
                                labels = taikunpycore.models.rule_labels.RuleLabels(
                                    severity = '', ), 
                                annotations = taikunpycore.models.annotations.Annotations(
                                    description = '', 
                                    title = '', ), 
                                alerts = [
                                    taikunpycore.models.alert.Alert(
                                        state = '', 
                                        active_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        value = '', )
                                    ], 
                                health = '', 
                                evaluation_time = 1.337, 
                                last_evaluation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                type = '', )
                            ], 
                        interval = 56, 
                        evaluation_time = 1.337, 
                        last_evaluation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return AlertData(
        )
        """

    def testAlertData(self):
        """Test AlertData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
