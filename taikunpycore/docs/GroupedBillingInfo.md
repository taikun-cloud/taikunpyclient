# GroupedBillingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GroupedBillings]**](GroupedBillings.md) |  | [optional] 
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.grouped_billing_info import GroupedBillingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedBillingInfo from a JSON string
grouped_billing_info_instance = GroupedBillingInfo.from_json(json)
# print the JSON string representation of the object
print(GroupedBillingInfo.to_json())

# convert the object into a dict
grouped_billing_info_dict = grouped_billing_info_instance.to_dict()
# create an instance of GroupedBillingInfo from a dict
grouped_billing_info_from_dict = GroupedBillingInfo.from_dict(grouped_billing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


