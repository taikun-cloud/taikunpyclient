# DashboardChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**OrganizationEntityForDashboard**](OrganizationEntityForDashboard.md) |  | [optional] 
**projects** | [**ProjectChartDto**](ProjectChartDto.md) |  | [optional] 
**cloud_credentials** | [**CredentialChartDto**](CredentialChartDto.md) |  | [optional] 
**servers** | [**ServerChartDto**](ServerChartDto.md) |  | [optional] 
**stand_alone_vms** | [**ServerChartDto**](ServerChartDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.dashboard_chart import DashboardChart

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardChart from a JSON string
dashboard_chart_instance = DashboardChart.from_json(json)
# print the JSON string representation of the object
print(DashboardChart.to_json())

# convert the object into a dict
dashboard_chart_dict = dashboard_chart_instance.to_dict()
# create an instance of DashboardChart from a dict
dashboard_chart_from_dict = DashboardChart.from_dict(dashboard_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


