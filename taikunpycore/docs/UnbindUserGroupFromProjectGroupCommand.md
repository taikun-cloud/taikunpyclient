# UnbindUserGroupFromProjectGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_group_id** | **int** |  | [optional] 
**user_group_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.unbind_user_group_from_project_group_command import UnbindUserGroupFromProjectGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindUserGroupFromProjectGroupCommand from a JSON string
unbind_user_group_from_project_group_command_instance = UnbindUserGroupFromProjectGroupCommand.from_json(json)
# print the JSON string representation of the object
print(UnbindUserGroupFromProjectGroupCommand.to_json())

# convert the object into a dict
unbind_user_group_from_project_group_command_dict = unbind_user_group_from_project_group_command_instance.to_dict()
# create an instance of UnbindUserGroupFromProjectGroupCommand from a dict
unbind_user_group_from_project_group_command_from_dict = UnbindUserGroupFromProjectGroupCommand.from_dict(unbind_user_group_from_project_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


