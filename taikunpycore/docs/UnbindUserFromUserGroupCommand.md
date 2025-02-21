# UnbindUserFromUserGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_id** | **int** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.unbind_user_from_user_group_command import UnbindUserFromUserGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindUserFromUserGroupCommand from a JSON string
unbind_user_from_user_group_command_instance = UnbindUserFromUserGroupCommand.from_json(json)
# print the JSON string representation of the object
print(UnbindUserFromUserGroupCommand.to_json())

# convert the object into a dict
unbind_user_from_user_group_command_dict = unbind_user_from_user_group_command_instance.to_dict()
# create an instance of UnbindUserFromUserGroupCommand from a dict
unbind_user_from_user_group_command_from_dict = UnbindUserFromUserGroupCommand.from_dict(unbind_user_from_user_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


