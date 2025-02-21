# CheckAzureCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_client_id** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_tenant_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.check_azure_command import CheckAzureCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAzureCommand from a JSON string
check_azure_command_instance = CheckAzureCommand.from_json(json)
# print the JSON string representation of the object
print(CheckAzureCommand.to_json())

# convert the object into a dict
check_azure_command_dict = check_azure_command_instance.to_dict()
# create an instance of CheckAzureCommand from a dict
check_azure_command_from_dict = CheckAzureCommand.from_dict(check_azure_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


