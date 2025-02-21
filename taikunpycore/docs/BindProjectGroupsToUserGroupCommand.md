# BindProjectGroupsToUserGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_groups** | **List[int]** |  | [optional] 
**user_group_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_project_groups_to_user_group_command import BindProjectGroupsToUserGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindProjectGroupsToUserGroupCommand from a JSON string
bind_project_groups_to_user_group_command_instance = BindProjectGroupsToUserGroupCommand.from_json(json)
# print the JSON string representation of the object
print(BindProjectGroupsToUserGroupCommand.to_json())

# convert the object into a dict
bind_project_groups_to_user_group_command_dict = bind_project_groups_to_user_group_command_instance.to_dict()
# create an instance of BindProjectGroupsToUserGroupCommand from a dict
bind_project_groups_to_user_group_command_from_dict = BindProjectGroupsToUserGroupCommand.from_dict(bind_project_groups_to_user_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


