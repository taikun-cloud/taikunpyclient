# CatalogAppParamsDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**catalog_app_name** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**is_editable_when_installing** | **bool** |  | [optional] 
**is_editable_after_installation** | **bool** |  | [optional] 
**is_mandatory** | **bool** |  | [optional] 
**has_json_schema** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_app_params_details_dto import CatalogAppParamsDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAppParamsDetailsDto from a JSON string
catalog_app_params_details_dto_instance = CatalogAppParamsDetailsDto.from_json(json)
# print the JSON string representation of the object
print(CatalogAppParamsDetailsDto.to_json())

# convert the object into a dict
catalog_app_params_details_dto_dict = catalog_app_params_details_dto_instance.to_dict()
# create an instance of CatalogAppParamsDetailsDto from a dict
catalog_app_params_details_dto_from_dict = CatalogAppParamsDetailsDto.from_dict(catalog_app_params_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


