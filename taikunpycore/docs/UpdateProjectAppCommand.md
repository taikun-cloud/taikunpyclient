# UpdateProjectAppCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_app_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_project_app_command import UpdateProjectAppCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectAppCommand from a JSON string
update_project_app_command_instance = UpdateProjectAppCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectAppCommand.to_json())

# convert the object into a dict
update_project_app_command_dict = update_project_app_command_instance.to_dict()
# create an instance of UpdateProjectAppCommand from a dict
update_project_app_command_from_dict = UpdateProjectAppCommand.from_dict(update_project_app_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


