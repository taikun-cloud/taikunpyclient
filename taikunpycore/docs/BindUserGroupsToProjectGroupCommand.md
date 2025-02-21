# BindUserGroupsToProjectGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_groups** | **List[int]** |  | [optional] 
**project_group_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_user_groups_to_project_group_command import BindUserGroupsToProjectGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindUserGroupsToProjectGroupCommand from a JSON string
bind_user_groups_to_project_group_command_instance = BindUserGroupsToProjectGroupCommand.from_json(json)
# print the JSON string representation of the object
print(BindUserGroupsToProjectGroupCommand.to_json())

# convert the object into a dict
bind_user_groups_to_project_group_command_dict = bind_user_groups_to_project_group_command_instance.to_dict()
# create an instance of BindUserGroupsToProjectGroupCommand from a dict
bind_user_groups_to_project_group_command_from_dict = BindUserGroupsToProjectGroupCommand.from_dict(bind_user_groups_to_project_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


