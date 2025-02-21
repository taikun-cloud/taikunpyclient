# ExecutorEntityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**health** | [**ExecutorHealth**](ExecutorHealth.md) |  | [optional] 
**kube_config** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.executor_entity_dto import ExecutorEntityDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutorEntityDto from a JSON string
executor_entity_dto_instance = ExecutorEntityDto.from_json(json)
# print the JSON string representation of the object
print(ExecutorEntityDto.to_json())

# convert the object into a dict
executor_entity_dto_dict = executor_entity_dto_instance.to_dict()
# create an instance of ExecutorEntityDto from a dict
executor_entity_dto_from_dict = ExecutorEntityDto.from_dict(executor_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


