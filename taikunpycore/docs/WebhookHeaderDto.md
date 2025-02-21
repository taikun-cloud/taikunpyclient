# WebhookHeaderDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.webhook_header_dto import WebhookHeaderDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookHeaderDto from a JSON string
webhook_header_dto_instance = WebhookHeaderDto.from_json(json)
# print the JSON string representation of the object
print(WebhookHeaderDto.to_json())

# convert the object into a dict
webhook_header_dto_dict = webhook_header_dto_instance.to_dict()
# create an instance of WebhookHeaderDto from a dict
webhook_header_dto_from_dict = WebhookHeaderDto.from_dict(webhook_header_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


