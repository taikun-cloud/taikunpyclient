# UpdateAzureCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**azure_client_secret** | **str** |  | [optional] 
**azure_client_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_azure_command import UpdateAzureCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAzureCommand from a JSON string
update_azure_command_instance = UpdateAzureCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateAzureCommand.to_json())

# convert the object into a dict
update_azure_command_dict = update_azure_command_instance.to_dict()
# create an instance of UpdateAzureCommand from a dict
update_azure_command_from_dict = UpdateAzureCommand.from_dict(update_azure_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


