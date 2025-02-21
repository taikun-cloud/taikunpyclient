# CommonStringDropdownIsBoundDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_bound** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.common_string_dropdown_is_bound_dto import CommonStringDropdownIsBoundDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonStringDropdownIsBoundDto from a JSON string
common_string_dropdown_is_bound_dto_instance = CommonStringDropdownIsBoundDto.from_json(json)
# print the JSON string representation of the object
print(CommonStringDropdownIsBoundDto.to_json())

# convert the object into a dict
common_string_dropdown_is_bound_dto_dict = common_string_dropdown_is_bound_dto_instance.to_dict()
# create an instance of CommonStringDropdownIsBoundDto from a dict
common_string_dropdown_is_bound_dto_from_dict = CommonStringDropdownIsBoundDto.from_dict(common_string_dropdown_is_bound_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


