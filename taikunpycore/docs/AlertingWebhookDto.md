# AlertingWebhookDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**headers** | [**List[WebhookHeaderDto]**](WebhookHeaderDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.alerting_webhook_dto import AlertingWebhookDto

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingWebhookDto from a JSON string
alerting_webhook_dto_instance = AlertingWebhookDto.from_json(json)
# print the JSON string representation of the object
print(AlertingWebhookDto.to_json())

# convert the object into a dict
alerting_webhook_dto_dict = alerting_webhook_dto_instance.to_dict()
# create an instance of AlertingWebhookDto from a dict
alerting_webhook_dto_from_dict = AlertingWebhookDto.from_dict(alerting_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


