# Breakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[Resource]**](Resource.md) |  | [optional] 
**total_hourly_cost** | **str** |  | [optional] 
**total_monthly_cost** | **str** |  | [optional] 
**total_monthly_usage_cost** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.breakdown import Breakdown

# TODO update the JSON string below
json = "{}"
# create an instance of Breakdown from a JSON string
breakdown_instance = Breakdown.from_json(json)
# print the JSON string representation of the object
print(Breakdown.to_json())

# convert the object into a dict
breakdown_dict = breakdown_instance.to_dict()
# create an instance of Breakdown from a dict
breakdown_from_dict = Breakdown.from_dict(breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


