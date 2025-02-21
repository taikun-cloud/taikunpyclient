# StripeSubscriptionItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_item_id** | **str** |  | 
**price_id** | **str** |  | 
**product_id** | **str** |  | 

## Example

```python
from taikunpycore.models.stripe_subscription_item_dto import StripeSubscriptionItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of StripeSubscriptionItemDto from a JSON string
stripe_subscription_item_dto_instance = StripeSubscriptionItemDto.from_json(json)
# print the JSON string representation of the object
print(StripeSubscriptionItemDto.to_json())

# convert the object into a dict
stripe_subscription_item_dto_dict = stripe_subscription_item_dto_instance.to_dict()
# create an instance of StripeSubscriptionItemDto from a dict
stripe_subscription_item_dto_from_dict = StripeSubscriptionItemDto.from_dict(stripe_subscription_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


