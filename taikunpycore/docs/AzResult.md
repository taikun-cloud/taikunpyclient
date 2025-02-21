# AzResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.az_result import AzResult

# TODO update the JSON string below
json = "{}"
# create an instance of AzResult from a JSON string
az_result_instance = AzResult.from_json(json)
# print the JSON string representation of the object
print(AzResult.to_json())

# convert the object into a dict
az_result_dict = az_result_instance.to_dict()
# create an instance of AzResult from a dict
az_result_from_dict = AzResult.from_dict(az_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


