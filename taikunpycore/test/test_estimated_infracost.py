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

from taikunpycore.models.estimated_infracost import EstimatedInfracost

class TestEstimatedInfracost(unittest.TestCase):
    """EstimatedInfracost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EstimatedInfracost:
        """Test EstimatedInfracost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimatedInfracost`
        """
        model = EstimatedInfracost()
        if include_optional:
            return EstimatedInfracost(
                version = '',
                metadata = taikunpycore.models.metadata.Metadata(
                    infracost_command = '', 
                    vcs_branch = '', 
                    vcs_commit_sha = '', 
                    vcs_commit_author_name = '', 
                    vcs_commit_author_email = '', 
                    vcs_commit_timestamp = '', 
                    vcs_commit_message = '', 
                    vcs_repository_url = '', 
                    usage_api_enabled = True, ),
                currency = '',
                projects = [
                    taikunpycore.models.project_infracost.ProjectInfracost(
                        name = '', 
                        display_name = '', 
                        metadata = taikunpycore.models.project_metadata.ProjectMetadata(
                            path = '', 
                            type = '', 
                            vcs_sub_path = '', 
                            providers = [
                                taikunpycore.models.provider.Provider(
                                    name = '', )
                                ], ), 
                        past_breakdown = taikunpycore.models.breakdown.Breakdown(
                            resources = [
                                taikunpycore.models.resource.Resource(
                                    name = '', 
                                    resource_type = '', 
                                    tags = {
                                        'key' : ''
                                        }, 
                                    hourly_cost = '', 
                                    monthly_cost = '', 
                                    monthly_usage_cost = '', 
                                    cost_components = [
                                        taikunpycore.models.cost_component.CostComponent(
                                            name = '', 
                                            unit = '', 
                                            hourly_quantity = '', 
                                            monthly_quantity = '', 
                                            price = '', 
                                            hourly_cost = '', 
                                            monthly_cost = '', 
                                            price_not_found = True, 
                                            usage_based = True, )
                                        ], 
                                    subresources = [
                                        taikunpycore.models.subresource.Subresource(
                                            name = '', 
                                            hourly_cost = '', 
                                            monthly_cost = '', )
                                        ], )
                                ], 
                            total_hourly_cost = '', 
                            total_monthly_cost = '', 
                            total_monthly_usage_cost = '', ), 
                        breakdown = taikunpycore.models.breakdown.Breakdown(
                            total_hourly_cost = '', 
                            total_monthly_cost = '', 
                            total_monthly_usage_cost = '', ), 
                        diff = taikunpycore.models.diff.Diff(
                            total_hourly_cost = '', 
                            total_monthly_cost = '', 
                            total_monthly_usage_cost = '', ), 
                        summary = taikunpycore.models.summary.Summary(
                            total_detected_resources = 56, 
                            total_supported_resources = 56, 
                            total_unsupported_resources = 56, 
                            total_usage_based_resources = 56, 
                            total_no_price_resources = 56, 
                            unsupported_resource_counts = {
                                'key' : 56
                                }, 
                            no_price_resource_counts = {
                                'key' : 56
                                }, ), )
                    ],
                total_hourly_cost = '',
                total_monthly_cost = '',
                total_monthly_usage_cost = '',
                past_total_hourly_cost = '',
                past_total_monthly_cost = '',
                past_total_monthly_usage_cost = '',
                diff_total_hourly_cost = '',
                diff_total_monthly_cost = '',
                diff_total_monthly_usage_cost = '',
                time_generated = '',
                summary = taikunpycore.models.summary.Summary(
                    total_detected_resources = 56, 
                    total_supported_resources = 56, 
                    total_unsupported_resources = 56, 
                    total_usage_based_resources = 56, 
                    total_no_price_resources = 56, 
                    unsupported_resource_counts = {
                        'key' : 56
                        }, 
                    no_price_resource_counts = {
                        'key' : 56
                        }, )
            )
        else:
            return EstimatedInfracost(
        )
        """

    def testEstimatedInfracost(self):
        """Test EstimatedInfracost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
