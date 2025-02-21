# RemindUsersByAlertingProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reminder** | [**AlertingReminder**](AlertingReminder.md) |  | [optional] 

## Example

```python
from taikunpycore.models.remind_users_by_alerting_profile_command import RemindUsersByAlertingProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RemindUsersByAlertingProfileCommand from a JSON string
remind_users_by_alerting_profile_command_instance = RemindUsersByAlertingProfileCommand.from_json(json)
# print the JSON string representation of the object
print(RemindUsersByAlertingProfileCommand.to_json())

# convert the object into a dict
remind_users_by_alerting_profile_command_dict = remind_users_by_alerting_profile_command_instance.to_dict()
# create an instance of RemindUsersByAlertingProfileCommand from a dict
remind_users_by_alerting_profile_command_from_dict = RemindUsersByAlertingProfileCommand.from_dict(remind_users_by_alerting_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


