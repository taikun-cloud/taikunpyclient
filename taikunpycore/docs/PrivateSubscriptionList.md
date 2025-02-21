# PrivateSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ListForPartnersDto]**](ListForPartnersDto.md) |  | 
**total_count** | **int** |  | 
**is_eligible_to_switch** | **bool** |  | 
**active_subscription_status** | **str** |  | 

## Example

```python
from taikunpycore.models.private_subscription_list import PrivateSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateSubscriptionList from a JSON string
private_subscription_list_instance = PrivateSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(PrivateSubscriptionList.to_json())

# convert the object into a dict
private_subscription_list_dict = private_subscription_list_instance.to_dict()
# create an instance of PrivateSubscriptionList from a dict
private_subscription_list_from_dict = PrivateSubscriptionList.from_dict(private_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


