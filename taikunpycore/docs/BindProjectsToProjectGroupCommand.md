# BindProjectsToProjectGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_group_id** | **int** |  | [optional] 
**project_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_projects_to_project_group_command import BindProjectsToProjectGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindProjectsToProjectGroupCommand from a JSON string
bind_projects_to_project_group_command_instance = BindProjectsToProjectGroupCommand.from_json(json)
# print the JSON string representation of the object
print(BindProjectsToProjectGroupCommand.to_json())

# convert the object into a dict
bind_projects_to_project_group_command_dict = bind_projects_to_project_group_command_instance.to_dict()
# create an instance of BindProjectsToProjectGroupCommand from a dict
bind_projects_to_project_group_command_from_dict = BindProjectsToProjectGroupCommand.from_dict(bind_projects_to_project_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


