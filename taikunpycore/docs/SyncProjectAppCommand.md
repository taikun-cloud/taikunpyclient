# SyncProjectAppCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_app_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.sync_project_app_command import SyncProjectAppCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SyncProjectAppCommand from a JSON string
sync_project_app_command_instance = SyncProjectAppCommand.from_json(json)
# print the JSON string representation of the object
print(SyncProjectAppCommand.to_json())

# convert the object into a dict
sync_project_app_command_dict = sync_project_app_command_instance.to_dict()
# create an instance of SyncProjectAppCommand from a dict
sync_project_app_command_from_dict = SyncProjectAppCommand.from_dict(sync_project_app_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


