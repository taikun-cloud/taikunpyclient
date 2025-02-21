# CommonDropdownIsBoundDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_bound** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.common_dropdown_is_bound_dto import CommonDropdownIsBoundDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDropdownIsBoundDto from a JSON string
common_dropdown_is_bound_dto_instance = CommonDropdownIsBoundDto.from_json(json)
# print the JSON string representation of the object
print(CommonDropdownIsBoundDto.to_json())

# convert the object into a dict
common_dropdown_is_bound_dto_dict = common_dropdown_is_bound_dto_instance.to_dict()
# create an instance of CommonDropdownIsBoundDto from a dict
common_dropdown_is_bound_dto_from_dict = CommonDropdownIsBoundDto.from_dict(common_dropdown_is_bound_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


