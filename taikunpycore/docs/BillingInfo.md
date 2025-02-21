# BillingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BillingSummaryDto]**](BillingSummaryDto.md) |  | [optional] 
**total_tcu** | **float** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.billing_info import BillingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInfo from a JSON string
billing_info_instance = BillingInfo.from_json(json)
# print the JSON string representation of the object
print(BillingInfo.to_json())

# convert the object into a dict
billing_info_dict = billing_info_instance.to_dict()
# create an instance of BillingInfo from a dict
billing_info_from_dict = BillingInfo.from_dict(billing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


