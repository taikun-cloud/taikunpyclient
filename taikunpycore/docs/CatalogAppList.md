# CatalogAppList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CatalogAppListDto]**](CatalogAppListDto.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_app_list import CatalogAppList

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAppList from a JSON string
catalog_app_list_instance = CatalogAppList.from_json(json)
# print the JSON string representation of the object
print(CatalogAppList.to_json())

# convert the object into a dict
catalog_app_list_dict = catalog_app_list_instance.to_dict()
# create an instance of CatalogAppList from a dict
catalog_app_list_from_dict = CatalogAppList.from_dict(catalog_app_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


