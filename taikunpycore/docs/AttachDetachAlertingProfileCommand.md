# AttachDetachAlertingProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**alerting_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.attach_detach_alerting_profile_command import AttachDetachAlertingProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AttachDetachAlertingProfileCommand from a JSON string
attach_detach_alerting_profile_command_instance = AttachDetachAlertingProfileCommand.from_json(json)
# print the JSON string representation of the object
print(AttachDetachAlertingProfileCommand.to_json())

# convert the object into a dict
attach_detach_alerting_profile_command_dict = attach_detach_alerting_profile_command_instance.to_dict()
# create an instance of AttachDetachAlertingProfileCommand from a dict
attach_detach_alerting_profile_command_from_dict = AttachDetachAlertingProfileCommand.from_dict(attach_detach_alerting_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


