# CommonExtendedDropdownDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.common_extended_dropdown_dto import CommonExtendedDropdownDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonExtendedDropdownDto from a JSON string
common_extended_dropdown_dto_instance = CommonExtendedDropdownDto.from_json(json)
# print the JSON string representation of the object
print(CommonExtendedDropdownDto.to_json())

# convert the object into a dict
common_extended_dropdown_dto_dict = common_extended_dropdown_dto_instance.to_dict()
# create an instance of CommonExtendedDropdownDto from a dict
common_extended_dropdown_dto_from_dict = CommonExtendedDropdownDto.from_dict(common_extended_dropdown_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


