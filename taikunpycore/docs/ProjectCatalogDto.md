# ProjectCatalogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**maintenance_mode_enabled** | **bool** |  | [optional] 
**is_virtual_cluster** | **bool** |  | [optional] 
**cloud_type** | [**CloudType**](CloudType.md) |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_catalog_dto import ProjectCatalogDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCatalogDto from a JSON string
project_catalog_dto_instance = ProjectCatalogDto.from_json(json)
# print the JSON string representation of the object
print(ProjectCatalogDto.to_json())

# convert the object into a dict
project_catalog_dto_dict = project_catalog_dto_instance.to_dict()
# create an instance of ProjectCatalogDto from a dict
project_catalog_dto_from_dict = ProjectCatalogDto.from_dict(project_catalog_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


