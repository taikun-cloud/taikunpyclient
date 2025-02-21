# AzureZonesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_subscription_id** | **str** |  | [optional] 
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_tenant_id** | **str** |  | [optional] 
**azure_location** | **str** |  | [optional] 
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_zones_command import AzureZonesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AzureZonesCommand from a JSON string
azure_zones_command_instance = AzureZonesCommand.from_json(json)
# print the JSON string representation of the object
print(AzureZonesCommand.to_json())

# convert the object into a dict
azure_zones_command_dict = azure_zones_command_instance.to_dict()
# create an instance of AzureZonesCommand from a dict
azure_zones_command_from_dict = AzureZonesCommand.from_dict(azure_zones_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


