# CatalogAppListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_app_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**repo_id** | **int** |  | [optional] 
**repo_name** | **str** |  | [optional] 
**catalog_id** | **int** |  | [optional] 
**catalog_name** | **str** |  | [optional] 
**package_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**logo_image_id** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**app_version** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**security_report_summary** | [**SecurityReportSummary**](SecurityReportSummary.md) |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**stars** | **int** |  | [optional] 
**installed_instance_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_app_list_dto import CatalogAppListDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAppListDto from a JSON string
catalog_app_list_dto_instance = CatalogAppListDto.from_json(json)
# print the JSON string representation of the object
print(CatalogAppListDto.to_json())

# convert the object into a dict
catalog_app_list_dto_dict = catalog_app_list_dto_instance.to_dict()
# create an instance of CatalogAppListDto from a dict
catalog_app_list_dto_from_dict = CatalogAppListDto.from_dict(catalog_app_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


