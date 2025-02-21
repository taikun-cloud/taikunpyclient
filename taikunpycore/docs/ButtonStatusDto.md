# ButtonStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**reasons** | **List[str]** |  | [optional] 
**hidden** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.button_status_dto import ButtonStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ButtonStatusDto from a JSON string
button_status_dto_instance = ButtonStatusDto.from_json(json)
# print the JSON string representation of the object
print(ButtonStatusDto.to_json())

# convert the object into a dict
button_status_dto_dict = button_status_dto_instance.to_dict()
# create an instance of ButtonStatusDto from a dict
button_status_dto_from_dict = ButtonStatusDto.from_dict(button_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


