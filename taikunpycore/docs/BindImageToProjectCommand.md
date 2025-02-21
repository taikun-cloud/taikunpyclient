# BindImageToProjectCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**images** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_image_to_project_command import BindImageToProjectCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindImageToProjectCommand from a JSON string
bind_image_to_project_command_instance = BindImageToProjectCommand.from_json(json)
# print the JSON string representation of the object
print(BindImageToProjectCommand.to_json())

# convert the object into a dict
bind_image_to_project_command_dict = bind_image_to_project_command_instance.to_dict()
# create an instance of BindImageToProjectCommand from a dict
bind_image_to_project_command_from_dict = BindImageToProjectCommand.from_dict(bind_image_to_project_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


