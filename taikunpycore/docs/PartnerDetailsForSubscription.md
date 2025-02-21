# PartnerDetailsForSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**logo** | **str** |  | 
**link** | **str** |  | 
**id** | **int** |  | 

## Example

```python
from taikunpycore.models.partner_details_for_subscription import PartnerDetailsForSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerDetailsForSubscription from a JSON string
partner_details_for_subscription_instance = PartnerDetailsForSubscription.from_json(json)
# print the JSON string representation of the object
print(PartnerDetailsForSubscription.to_json())

# convert the object into a dict
partner_details_for_subscription_dict = partner_details_for_subscription_instance.to_dict()
# create an instance of PartnerDetailsForSubscription from a dict
partner_details_for_subscription_from_dict = PartnerDetailsForSubscription.from_dict(partner_details_for_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


