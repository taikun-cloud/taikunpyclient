# CatalogList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CatalogListDto]**](CatalogListDto.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_list import CatalogList

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogList from a JSON string
catalog_list_instance = CatalogList.from_json(json)
# print the JSON string representation of the object
print(CatalogList.to_json())

# convert the object into a dict
catalog_list_dict = catalog_list_instance.to_dict()
# create an instance of CatalogList from a dict
catalog_list_from_dict = CatalogList.from_dict(catalog_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


