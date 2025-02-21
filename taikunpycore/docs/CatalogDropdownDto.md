# CatalogDropdownDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**package_ids** | **List[str]** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_dropdown_dto import CatalogDropdownDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogDropdownDto from a JSON string
catalog_dropdown_dto_instance = CatalogDropdownDto.from_json(json)
# print the JSON string representation of the object
print(CatalogDropdownDto.to_json())

# convert the object into a dict
catalog_dropdown_dto_dict = catalog_dropdown_dto_instance.to_dict()
# create an instance of CatalogDropdownDto from a dict
catalog_dropdown_dto_from_dict = CatalogDropdownDto.from_dict(catalog_dropdown_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


