# CatalogAppParamsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**is_editable_when_installing** | **bool** |  | [optional] 
**is_editable_after_installation** | **bool** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_app_params_dto import CatalogAppParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAppParamsDto from a JSON string
catalog_app_params_dto_instance = CatalogAppParamsDto.from_json(json)
# print the JSON string representation of the object
print(CatalogAppParamsDto.to_json())

# convert the object into a dict
catalog_app_params_dto_dict = catalog_app_params_dto_instance.to_dict()
# create an instance of CatalogAppParamsDto from a dict
catalog_app_params_dto_from_dict = CatalogAppParamsDto.from_dict(catalog_app_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


