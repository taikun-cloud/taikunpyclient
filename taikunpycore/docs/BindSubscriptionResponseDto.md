# BindSubscriptionResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**payment_intent_client_secret** | **str** |  | [optional] 
**payment_intent_id** | **str** |  | [optional] 
**invoice_failure_code** | **str** |  | [optional] 
**invoice_failure_message** | **str** |  | [optional] 
**invoice_failure_reason** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_subscription_response_dto import BindSubscriptionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BindSubscriptionResponseDto from a JSON string
bind_subscription_response_dto_instance = BindSubscriptionResponseDto.from_json(json)
# print the JSON string representation of the object
print(BindSubscriptionResponseDto.to_json())

# convert the object into a dict
bind_subscription_response_dto_dict = bind_subscription_response_dto_instance.to_dict()
# create an instance of BindSubscriptionResponseDto from a dict
bind_subscription_response_dto_from_dict = BindSubscriptionResponseDto.from_dict(bind_subscription_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


