# ToggleNotificationModeCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.toggle_notification_mode_command import ToggleNotificationModeCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleNotificationModeCommand from a JSON string
toggle_notification_mode_command_instance = ToggleNotificationModeCommand.from_json(json)
# print the JSON string representation of the object
print(ToggleNotificationModeCommand.to_json())

# convert the object into a dict
toggle_notification_mode_command_dict = toggle_notification_mode_command_instance.to_dict()
# create an instance of ToggleNotificationModeCommand from a dict
toggle_notification_mode_command_from_dict = ToggleNotificationModeCommand.from_dict(toggle_notification_mode_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


