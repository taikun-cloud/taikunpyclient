# AlertingIntegrationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**token** | **str** |  | 
**alerting_integration_type** | [**AlertingIntegrationType**](AlertingIntegrationType.md) |  | 

## Example

```python
from taikunpycore.models.alerting_integration_dto import AlertingIntegrationDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingIntegrationDto from a JSON string
alerting_integration_dto_instance = AlertingIntegrationDto.from_json(json)
# print the JSON string representation of the object
print(AlertingIntegrationDto.to_json())

# convert the object into a dict
alerting_integration_dto_dict = alerting_integration_dto_instance.to_dict()
# create an instance of AlertingIntegrationDto from a dict
alerting_integration_dto_from_dict = AlertingIntegrationDto.from_dict(alerting_integration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


