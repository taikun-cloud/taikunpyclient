# ProjectAppParamDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 
**is_editable_when_installing** | **bool** |  | 
**is_editable_after_installation** | **bool** |  | 
**is_mandatory** | **bool** |  | 

## Example

```python
from taikunpycore.models.project_app_param_dto import ProjectAppParamDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAppParamDto from a JSON string
project_app_param_dto_instance = ProjectAppParamDto.from_json(json)
# print the JSON string representation of the object
print(ProjectAppParamDto.to_json())

# convert the object into a dict
project_app_param_dto_dict = project_app_param_dto_instance.to_dict()
# create an instance of ProjectAppParamDto from a dict
project_app_param_dto_from_dict = ProjectAppParamDto.from_dict(project_app_param_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


