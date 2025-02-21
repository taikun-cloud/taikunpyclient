# GroupedPrometheusBillingListQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**period_duration** | [**BillingPeriod**](BillingPeriod.md) |  | [optional] 

## Example

```python
from taikunpycore.models.grouped_prometheus_billing_list_query import GroupedPrometheusBillingListQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedPrometheusBillingListQuery from a JSON string
grouped_prometheus_billing_list_query_instance = GroupedPrometheusBillingListQuery.from_json(json)
# print the JSON string representation of the object
print(GroupedPrometheusBillingListQuery.to_json())

# convert the object into a dict
grouped_prometheus_billing_list_query_dict = grouped_prometheus_billing_list_query_instance.to_dict()
# create an instance of GroupedPrometheusBillingListQuery from a dict
grouped_prometheus_billing_list_query_from_dict = GroupedPrometheusBillingListQuery.from_dict(grouped_prometheus_billing_list_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


