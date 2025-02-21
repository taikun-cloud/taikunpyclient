# EditProjectAppParamsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_project_app_params_dto import EditProjectAppParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditProjectAppParamsDto from a JSON string
edit_project_app_params_dto_instance = EditProjectAppParamsDto.from_json(json)
# print the JSON string representation of the object
print(EditProjectAppParamsDto.to_json())

# convert the object into a dict
edit_project_app_params_dto_dict = edit_project_app_params_dto_instance.to_dict()
# create an instance of EditProjectAppParamsDto from a dict
edit_project_app_params_dto_from_dict = EditProjectAppParamsDto.from_dict(edit_project_app_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


