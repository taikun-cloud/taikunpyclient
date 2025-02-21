# PrometheusBillingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PrometheusBillingSummaryDto]**](PrometheusBillingSummaryDto.md) |  | 
**total_price** | **float** |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.prometheus_billing_info import PrometheusBillingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusBillingInfo from a JSON string
prometheus_billing_info_instance = PrometheusBillingInfo.from_json(json)
# print the JSON string representation of the object
print(PrometheusBillingInfo.to_json())

# convert the object into a dict
prometheus_billing_info_dict = prometheus_billing_info_instance.to_dict()
# create an instance of PrometheusBillingInfo from a dict
prometheus_billing_info_from_dict = PrometheusBillingInfo.from_dict(prometheus_billing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


