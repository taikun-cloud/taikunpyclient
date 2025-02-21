# ExecutorListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExecutorEntityDto]**](ExecutorEntityDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.executor_list_response import ExecutorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutorListResponse from a JSON string
executor_list_response_instance = ExecutorListResponse.from_json(json)
# print the JSON string representation of the object
print(ExecutorListResponse.to_json())

# convert the object into a dict
executor_list_response_dict = executor_list_response_instance.to_dict()
# create an instance of ExecutorListResponse from a dict
executor_list_response_from_dict = ExecutorListResponse.from_dict(executor_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


