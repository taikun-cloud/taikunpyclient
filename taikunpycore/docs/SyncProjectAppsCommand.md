# SyncProjectAppsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_app_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.sync_project_apps_command import SyncProjectAppsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SyncProjectAppsCommand from a JSON string
sync_project_apps_command_instance = SyncProjectAppsCommand.from_json(json)
# print the JSON string representation of the object
print(SyncProjectAppsCommand.to_json())

# convert the object into a dict
sync_project_apps_command_dict = sync_project_apps_command_instance.to_dict()
# create an instance of SyncProjectAppsCommand from a dict
sync_project_apps_command_from_dict = SyncProjectAppsCommand.from_dict(sync_project_apps_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


