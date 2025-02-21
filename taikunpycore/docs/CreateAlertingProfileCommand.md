# CreateAlertingProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slack_configuration_id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**emails** | [**List[AlertingEmailDto]**](AlertingEmailDto.md) |  | [optional] 
**webhooks** | [**List[AlertingWebhookDto]**](AlertingWebhookDto.md) |  | [optional] 
**alerting_integrations** | [**List[AlertingIntegrationDto]**](AlertingIntegrationDto.md) |  | [optional] 
**reminder** | [**AlertingReminder**](AlertingReminder.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_alerting_profile_command import CreateAlertingProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertingProfileCommand from a JSON string
create_alerting_profile_command_instance = CreateAlertingProfileCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAlertingProfileCommand.to_json())

# convert the object into a dict
create_alerting_profile_command_dict = create_alerting_profile_command_instance.to_dict()
# create an instance of CreateAlertingProfileCommand from a dict
create_alerting_profile_command_from_dict = CreateAlertingProfileCommand.from_dict(create_alerting_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


