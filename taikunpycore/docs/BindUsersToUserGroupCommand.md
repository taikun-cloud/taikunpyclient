# BindUsersToUserGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_id** | **int** |  | [optional] 
**user_ids** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_users_to_user_group_command import BindUsersToUserGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindUsersToUserGroupCommand from a JSON string
bind_users_to_user_group_command_instance = BindUsersToUserGroupCommand.from_json(json)
# print the JSON string representation of the object
print(BindUsersToUserGroupCommand.to_json())

# convert the object into a dict
bind_users_to_user_group_command_dict = bind_users_to_user_group_command_instance.to_dict()
# create an instance of BindUsersToUserGroupCommand from a dict
bind_users_to_user_group_command_from_dict = BindUsersToUserGroupCommand.from_dict(bind_users_to_user_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


