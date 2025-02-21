# ProjectAppParamsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.project_app_params_dto import ProjectAppParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAppParamsDto from a JSON string
project_app_params_dto_instance = ProjectAppParamsDto.from_json(json)
# print the JSON string representation of the object
print(ProjectAppParamsDto.to_json())

# convert the object into a dict
project_app_params_dto_dict = project_app_params_dto_instance.to_dict()
# create an instance of ProjectAppParamsDto from a dict
project_app_params_dto_from_dict = ProjectAppParamsDto.from_dict(project_app_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


