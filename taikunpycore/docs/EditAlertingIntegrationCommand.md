# EditAlertingIntegrationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**alerting_integration_type** | [**AlertingIntegrationType**](AlertingIntegrationType.md) |  | [optional] 
**alerting_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_alerting_integration_command import EditAlertingIntegrationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditAlertingIntegrationCommand from a JSON string
edit_alerting_integration_command_instance = EditAlertingIntegrationCommand.from_json(json)
# print the JSON string representation of the object
print(EditAlertingIntegrationCommand.to_json())

# convert the object into a dict
edit_alerting_integration_command_dict = edit_alerting_integration_command_instance.to_dict()
# create an instance of EditAlertingIntegrationCommand from a dict
edit_alerting_integration_command_from_dict = EditAlertingIntegrationCommand.from_dict(edit_alerting_integration_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


