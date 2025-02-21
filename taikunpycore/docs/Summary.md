# Summary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_detected_resources** | **int** |  | [optional] 
**total_supported_resources** | **int** |  | [optional] 
**total_unsupported_resources** | **int** |  | [optional] 
**total_usage_based_resources** | **int** |  | [optional] 
**total_no_price_resources** | **int** |  | [optional] 
**unsupported_resource_counts** | **Dict[str, int]** |  | [optional] 
**no_price_resource_counts** | **Dict[str, int]** |  | [optional] 

## Example

```python
from taikunpycore.models.summary import Summary

# TODO update the JSON string below
json = "{}"
# create an instance of Summary from a JSON string
summary_instance = Summary.from_json(json)
# print the JSON string representation of the object
print(Summary.to_json())

# convert the object into a dict
summary_dict = summary_instance.to_dict()
# create an instance of Summary from a dict
summary_from_dict = Summary.from_dict(summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


