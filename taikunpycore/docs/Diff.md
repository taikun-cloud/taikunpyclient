# Diff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[Resource]**](Resource.md) |  | [optional] 
**total_hourly_cost** | **str** |  | [optional] 
**total_monthly_cost** | **str** |  | [optional] 
**total_monthly_usage_cost** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.diff import Diff

# TODO update the JSON string below
json = "{}"
# create an instance of Diff from a JSON string
diff_instance = Diff.from_json(json)
# print the JSON string representation of the object
print(Diff.to_json())

# convert the object into a dict
diff_dict = diff_instance.to_dict()
# create an instance of Diff from a dict
diff_from_dict = Diff.from_dict(diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


