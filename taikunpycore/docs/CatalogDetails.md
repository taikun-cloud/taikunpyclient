# CatalogDetails


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
from taikunpycore.models.catalog_details import CatalogDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogDetails from a JSON string
catalog_details_instance = CatalogDetails.from_json(json)
# print the JSON string representation of the object
print(CatalogDetails.to_json())

# convert the object into a dict
catalog_details_dict = catalog_details_instance.to_dict()
# create an instance of CatalogDetails from a dict
catalog_details_from_dict = CatalogDetails.from_dict(catalog_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


