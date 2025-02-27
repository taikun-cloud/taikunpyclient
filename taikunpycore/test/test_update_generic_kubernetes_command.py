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

from taikunpycore.models.update_generic_kubernetes_command import UpdateGenericKubernetesCommand

class TestUpdateGenericKubernetesCommand(unittest.TestCase):
    """UpdateGenericKubernetesCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateGenericKubernetesCommand:
        """Test UpdateGenericKubernetesCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateGenericKubernetesCommand`
        """
        model = UpdateGenericKubernetesCommand()
        if include_optional:
            return UpdateGenericKubernetesCommand(
                id = 56,
                name = ''
            )
        else:
            return UpdateGenericKubernetesCommand(
        )
        """

    def testUpdateGenericKubernetesCommand(self):
        """Test UpdateGenericKubernetesCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
