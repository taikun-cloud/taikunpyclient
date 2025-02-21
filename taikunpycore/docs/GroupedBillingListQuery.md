# GroupedBillingListQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**period_duration** | [**BillingPeriod**](BillingPeriod.md) |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.grouped_billing_list_query import GroupedBillingListQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedBillingListQuery from a JSON string
grouped_billing_list_query_instance = GroupedBillingListQuery.from_json(json)
# print the JSON string representation of the object
print(GroupedBillingListQuery.to_json())

# convert the object into a dict
grouped_billing_list_query_dict = grouped_billing_list_query_instance.to_dict()
# create an instance of GroupedBillingListQuery from a dict
grouped_billing_list_query_from_dict = GroupedBillingListQuery.from_dict(grouped_billing_list_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


