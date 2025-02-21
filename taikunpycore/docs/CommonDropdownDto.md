# CommonDropdownDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.common_dropdown_dto import CommonDropdownDto

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDropdownDto from a JSON string
common_dropdown_dto_instance = CommonDropdownDto.from_json(json)
# print the JSON string representation of the object
print(CommonDropdownDto.to_json())

# convert the object into a dict
common_dropdown_dto_dict = common_dropdown_dto_instance.to_dict()
# create an instance of CommonDropdownDto from a dict
common_dropdown_dto_from_dict = CommonDropdownDto.from_dict(common_dropdown_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


