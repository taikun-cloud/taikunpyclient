# AlertingIntegrationsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**token** | **str** |  | 
**alerting_integration_type** | [**AlertingIntegrationType**](AlertingIntegrationType.md) |  | 
**alerting_profile_name** | **str** |  | 

## Example

```python
from taikunpycore.models.alerting_integrations_list_dto import AlertingIntegrationsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingIntegrationsListDto from a JSON string
alerting_integrations_list_dto_instance = AlertingIntegrationsListDto.from_json(json)
# print the JSON string representation of the object
print(AlertingIntegrationsListDto.to_json())

# convert the object into a dict
alerting_integrations_list_dto_dict = alerting_integrations_list_dto_instance.to_dict()
# create an instance of AlertingIntegrationsListDto from a dict
alerting_integrations_list_dto_from_dict = AlertingIntegrationsListDto.from_dict(alerting_integrations_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


