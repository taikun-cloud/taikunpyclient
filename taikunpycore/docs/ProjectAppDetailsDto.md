# ProjectAppDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**status** | [**EInstanceStatus**](EInstanceStatus.md) |  | 
**version** | **str** |  | 
**catalog_id** | **int** |  | 
**catalog_name** | **str** |  | 
**catalog_app_name** | **str** |  | 
**app_repo_name** | **str** |  | 
**logo** | **str** |  | 
**values** | **str** |  | 
**auto_sync** | **bool** |  | 
**release_notes** | **str** |  | 
**project_name** | **str** |  | 
**helm_result** | **str** |  | 
**project_id** | **int** |  | 
**has_json_schema** | **bool** |  | 
**catalog_app_id** | **int** |  | 
**package_id** | **str** |  | 
**logs** | **str** |  | 
**project_app_params** | [**List[ProjectAppParamDto]**](ProjectAppParamDto.md) |  | 

## Example

```python
from taikunpycore.models.project_app_details_dto import ProjectAppDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAppDetailsDto from a JSON string
project_app_details_dto_instance = ProjectAppDetailsDto.from_json(json)
# print the JSON string representation of the object
print(ProjectAppDetailsDto.to_json())

# convert the object into a dict
project_app_details_dto_dict = project_app_details_dto_instance.to_dict()
# create an instance of ProjectAppDetailsDto from a dict
project_app_details_dto_from_dict = ProjectAppDetailsDto.from_dict(project_app_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


