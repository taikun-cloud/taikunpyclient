# CommonStringBasedDropdownDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.common_string_based_dropdown_dto import CommonStringBasedDropdownDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonStringBasedDropdownDto from a JSON string
common_string_based_dropdown_dto_instance = CommonStringBasedDropdownDto.from_json(json)
# print the JSON string representation of the object
print(CommonStringBasedDropdownDto.to_json())

# convert the object into a dict
common_string_based_dropdown_dto_dict = common_string_based_dropdown_dto_instance.to_dict()
# create an instance of CommonStringBasedDropdownDto from a dict
common_string_based_dropdown_dto_from_dict = CommonStringBasedDropdownDto.from_dict(common_string_based_dropdown_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


