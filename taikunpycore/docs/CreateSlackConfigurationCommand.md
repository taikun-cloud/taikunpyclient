# CreateSlackConfigurationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**slack_type** | [**SlackType**](SlackType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_slack_configuration_command import CreateSlackConfigurationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSlackConfigurationCommand from a JSON string
create_slack_configuration_command_instance = CreateSlackConfigurationCommand.from_json(json)
# print the JSON string representation of the object
print(CreateSlackConfigurationCommand.to_json())

# convert the object into a dict
create_slack_configuration_command_dict = create_slack_configuration_command_instance.to_dict()
# create an instance of CreateSlackConfigurationCommand from a dict
create_slack_configuration_command_from_dict = CreateSlackConfigurationCommand.from_dict(create_slack_configuration_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


