# ProjectAppDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**status** | [**EInstanceStatus**](EInstanceStatus.md) |  | [optional] 
**auto_sync** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.project_app_dto import ProjectAppDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAppDto from a JSON string
project_app_dto_instance = ProjectAppDto.from_json(json)
# print the JSON string representation of the object
print(ProjectAppDto.to_json())

# convert the object into a dict
project_app_dto_dict = project_app_dto_instance.to_dict()
# create an instance of ProjectAppDto from a dict
project_app_dto_from_dict = ProjectAppDto.from_dict(project_app_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


