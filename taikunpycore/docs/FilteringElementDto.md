# FilteringElementDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.filtering_element_dto import FilteringElementDto

# TODO update the JSON string below
json = "{}"
# create an instance of FilteringElementDto from a JSON string
filtering_element_dto_instance = FilteringElementDto.from_json(json)
# print the JSON string representation of the object
print(FilteringElementDto.to_json())

# convert the object into a dict
filtering_element_dto_dict = filtering_element_dto_instance.to_dict()
# create an instance of FilteringElementDto from a dict
filtering_element_dto_from_dict = FilteringElementDto.from_dict(filtering_element_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


