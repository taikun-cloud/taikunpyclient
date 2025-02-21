# UnbindProjectGroupFromUserGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_id** | **int** |  | [optional] 
**project_group_ids** | **List[int]** |  | [optional] 

## Example

```python
from taikunpycore.models.unbind_project_group_from_user_group_command import UnbindProjectGroupFromUserGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindProjectGroupFromUserGroupCommand from a JSON string
unbind_project_group_from_user_group_command_instance = UnbindProjectGroupFromUserGroupCommand.from_json(json)
# print the JSON string representation of the object
print(UnbindProjectGroupFromUserGroupCommand.to_json())

# convert the object into a dict
unbind_project_group_from_user_group_command_dict = unbind_project_group_from_user_group_command_instance.to_dict()
# create an instance of UnbindProjectGroupFromUserGroupCommand from a dict
unbind_project_group_from_user_group_command_from_dict = UnbindProjectGroupFromUserGroupCommand.from_dict(unbind_project_group_from_user_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


