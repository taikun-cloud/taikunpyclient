# NotificationSendCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**action_type** | [**ActionType**](ActionType.md) |  | [optional] 
**action_status** | [**ActionStatus**](ActionStatus.md) |  | [optional] 
**project_type** | [**ProjectType**](ProjectType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.notification_send_command import NotificationSendCommand

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSendCommand from a JSON string
notification_send_command_instance = NotificationSendCommand.from_json(json)
# print the JSON string representation of the object
print(NotificationSendCommand.to_json())

# convert the object into a dict
notification_send_command_dict = notification_send_command_instance.to_dict()
# create an instance of NotificationSendCommand from a dict
notification_send_command_from_dict = NotificationSendCommand.from_dict(notification_send_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


