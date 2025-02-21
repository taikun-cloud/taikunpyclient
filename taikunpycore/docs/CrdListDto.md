# CrdListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**spec_name_kind** | **str** |  | 
**list_kind** | **str** |  | 
**group** | **str** |  | 
**labels** | **object** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.crd_list_dto import CrdListDto

# TODO update the JSON string below
json = "{}"
# create an instance of CrdListDto from a JSON string
crd_list_dto_instance = CrdListDto.from_json(json)
# print the JSON string representation of the object
print(CrdListDto.to_json())

# convert the object into a dict
crd_list_dto_dict = crd_list_dto_instance.to_dict()
# create an instance of CrdListDto from a dict
crd_list_dto_from_dict = CrdListDto.from_dict(crd_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


