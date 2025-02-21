# CatalogAppDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**app_repo_name** | **str** |  | [optional] 
**app_repo_organization_name** | **str** |  | [optional] 
**app_repo_id** | **int** |  | [optional] 
**catalog_name** | **str** |  | [optional] 
**catalog_id** | **int** |  | [optional] 
**package_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**logo_id** | **str** |  | [optional] 
**project_apps** | [**List[ProjectAppDto]**](ProjectAppDto.md) |  | [optional] 
**description** | **str** |  | [optional] 
**readme** | **str** |  | [optional] 
**security_report** | [**SecurityReportSummaryDto**](SecurityReportSummaryDto.md) |  | [optional] 
**app_version** | **str** |  | [optional] 
**stars** | **int** |  | [optional] 
**verified_publisher** | **bool** |  | [optional] 
**official** | **bool** |  | [optional] 
**has_json_schema** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_app_details_dto import CatalogAppDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogAppDetailsDto from a JSON string
catalog_app_details_dto_instance = CatalogAppDetailsDto.from_json(json)
# print the JSON string representation of the object
print(CatalogAppDetailsDto.to_json())

# convert the object into a dict
catalog_app_details_dto_dict = catalog_app_details_dto_instance.to_dict()
# create an instance of CatalogAppDetailsDto from a dict
catalog_app_details_dto_from_dict = CatalogAppDetailsDto.from_dict(catalog_app_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


