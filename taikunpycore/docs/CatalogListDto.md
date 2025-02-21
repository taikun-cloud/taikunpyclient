# CatalogListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**package_ids** | **List[str]** |  | [optional] 
**bound_projects** | [**List[ProjectCatalogDto]**](ProjectCatalogDto.md) |  | [optional] 
**bound_applications** | [**List[AvailablePackagesDto]**](AvailablePackagesDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_list_dto import CatalogListDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogListDto from a JSON string
catalog_list_dto_instance = CatalogListDto.from_json(json)
# print the JSON string representation of the object
print(CatalogListDto.to_json())

# convert the object into a dict
catalog_list_dto_dict = catalog_list_dto_instance.to_dict()
# create an instance of CatalogListDto from a dict
catalog_list_dto_from_dict = CatalogListDto.from_dict(catalog_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


