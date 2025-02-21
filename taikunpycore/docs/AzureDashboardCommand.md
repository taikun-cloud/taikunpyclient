# AzureDashboardCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 
**filter_by** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_dashboard_command import AzureDashboardCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDashboardCommand from a JSON string
azure_dashboard_command_instance = AzureDashboardCommand.from_json(json)
# print the JSON string representation of the object
print(AzureDashboardCommand.to_json())

# convert the object into a dict
azure_dashboard_command_dict = azure_dashboard_command_instance.to_dict()
# create an instance of AzureDashboardCommand from a dict
azure_dashboard_command_from_dict = AzureDashboardCommand.from_dict(azure_dashboard_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


