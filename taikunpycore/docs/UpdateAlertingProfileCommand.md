# UpdateAlertingProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**slack_configuration_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**reminder** | [**AlertingReminder**](AlertingReminder.md) |  | [optional] 

## Example

```python
from taikunpycore.models.update_alerting_profile_command import UpdateAlertingProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlertingProfileCommand from a JSON string
update_alerting_profile_command_instance = UpdateAlertingProfileCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateAlertingProfileCommand.to_json())

# convert the object into a dict
update_alerting_profile_command_dict = update_alerting_profile_command_instance.to_dict()
# create an instance of UpdateAlertingProfileCommand from a dict
update_alerting_profile_command_from_dict = UpdateAlertingProfileCommand.from_dict(update_alerting_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


