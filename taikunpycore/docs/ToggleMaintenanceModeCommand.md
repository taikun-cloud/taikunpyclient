# ToggleMaintenanceModeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.toggle_maintenance_mode_command import ToggleMaintenanceModeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleMaintenanceModeCommand from a JSON string
toggle_maintenance_mode_command_instance = ToggleMaintenanceModeCommand.from_json(json)
# print the JSON string representation of the object
print(ToggleMaintenanceModeCommand.to_json())

# convert the object into a dict
toggle_maintenance_mode_command_dict = toggle_maintenance_mode_command_instance.to_dict()
# create an instance of ToggleMaintenanceModeCommand from a dict
toggle_maintenance_mode_command_from_dict = ToggleMaintenanceModeCommand.from_dict(toggle_maintenance_mode_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


