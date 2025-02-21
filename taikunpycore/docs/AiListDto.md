# AiListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.ai_list_dto import AiListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiListDto from a JSON string
ai_list_dto_instance = AiListDto.from_json(json)
# print the JSON string representation of the object
print(AiListDto.to_json())

# convert the object into a dict
ai_list_dto_dict = ai_list_dto_instance.to_dict()
# create an instance of AiListDto from a dict
ai_list_dto_from_dict = AiListDto.from_dict(ai_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


