# OperationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**operation** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.operation_dto import OperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDto from a JSON string
operation_dto_instance = OperationDto.from_json(json)
# print the JSON string representation of the object
print(OperationDto.to_json())

# convert the object into a dict
operation_dto_dict = operation_dto_instance.to_dict()
# create an instance of OperationDto from a dict
operation_dto_from_dict = OperationDto.from_dict(operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


