# CreateAlertingIntegrationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**alerting_integration_type** | [**AlertingIntegrationType**](AlertingIntegrationType.md) |  | [optional] 
**alerting_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_alerting_integration_command import CreateAlertingIntegrationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlertingIntegrationCommand from a JSON string
create_alerting_integration_command_instance = CreateAlertingIntegrationCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAlertingIntegrationCommand.to_json())

# convert the object into a dict
create_alerting_integration_command_dict = create_alerting_integration_command_instance.to_dict()
# create an instance of CreateAlertingIntegrationCommand from a dict
create_alerting_integration_command_from_dict = CreateAlertingIntegrationCommand.from_dict(create_alerting_integration_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


