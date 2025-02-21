# LokiResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**limit** | **int** |  | [optional] 
**direction** | **str** |  | [optional] 
**can_download** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.loki_response_dto import LokiResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LokiResponseDto from a JSON string
loki_response_dto_instance = LokiResponseDto.from_json(json)
# print the JSON string representation of the object
print(LokiResponseDto.to_json())

# convert the object into a dict
loki_response_dto_dict = loki_response_dto_instance.to_dict()
# create an instance of LokiResponseDto from a dict
loki_response_dto_from_dict = LokiResponseDto.from_dict(loki_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


