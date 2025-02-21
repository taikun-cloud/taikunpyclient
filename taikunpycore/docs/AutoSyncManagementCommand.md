# AutoSyncManagementCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.auto_sync_management_command import AutoSyncManagementCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AutoSyncManagementCommand from a JSON string
auto_sync_management_command_instance = AutoSyncManagementCommand.from_json(json)
# print the JSON string representation of the object
print(AutoSyncManagementCommand.to_json())

# convert the object into a dict
auto_sync_management_command_dict = auto_sync_management_command_instance.to_dict()
# create an instance of AutoSyncManagementCommand from a dict
auto_sync_management_command_from_dict = AutoSyncManagementCommand.from_dict(auto_sync_management_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


