# AzureLocationsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_subscription_id** | **str** |  | [optional] 
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_tenant_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_locations_command import AzureLocationsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AzureLocationsCommand from a JSON string
azure_locations_command_instance = AzureLocationsCommand.from_json(json)
# print the JSON string representation of the object
print(AzureLocationsCommand.to_json())

# convert the object into a dict
azure_locations_command_dict = azure_locations_command_instance.to_dict()
# create an instance of AzureLocationsCommand from a dict
azure_locations_command_from_dict = AzureLocationsCommand.from_dict(azure_locations_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


