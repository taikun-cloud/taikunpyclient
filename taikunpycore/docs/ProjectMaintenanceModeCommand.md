# ProjectMaintenanceModeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.project_maintenance_mode_command import ProjectMaintenanceModeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMaintenanceModeCommand from a JSON string
project_maintenance_mode_command_instance = ProjectMaintenanceModeCommand.from_json(json)
# print the JSON string representation of the object
print(ProjectMaintenanceModeCommand.to_json())

# convert the object into a dict
project_maintenance_mode_command_dict = project_maintenance_mode_command_instance.to_dict()
# create an instance of ProjectMaintenanceModeCommand from a dict
project_maintenance_mode_command_from_dict = ProjectMaintenanceModeCommand.from_dict(project_maintenance_mode_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


